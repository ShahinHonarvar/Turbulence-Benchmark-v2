def all_left_right_truncatable_prime(numbers):
    x = numbers[760]

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable_prime(n):
        if n < 10 or '0' in str(n) or (not is_prime(n)):
            return False
        left_truncations = [int(str(n)[i:]) for i in range(len(str(n)))]
        right_truncations = [int(str(n)[:i]) for i in range(1, len(str(n)) + 1)]
        for num in left_truncations + right_truncations:
            if not is_prime(num):
                return False
        return True
    result = []
    for i in range(2, x + 1):
        if is_left_right_truncatable_prime(i):
            result.append(i)
    result.sort(reverse=True)
    return result