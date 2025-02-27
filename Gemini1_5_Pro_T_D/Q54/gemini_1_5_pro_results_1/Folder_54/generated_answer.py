def all_right_truncatable_prime(numbers):
    x = numbers[88]

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        if n < 10 and is_prime(n):
            return True
        if not is_prime(n):
            return False
        return is_right_truncatable_prime(n // 10)
    result = []
    for i in range(2, x):
        if is_right_truncatable_prime(i):
            result.append(i)
    result.sort(reverse=True)
    return result