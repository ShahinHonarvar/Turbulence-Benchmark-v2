def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        if n < 10:
            return is_prime(n)
        return is_prime(n) and '0' not in str(n) and is_left_truncatable_prime(int(str(n)[1:]))
    x = numbers[26]
    result = []
    for num in range(2, x):
        if is_left_truncatable_prime(num):
            result.append(num)
    return sorted(result)