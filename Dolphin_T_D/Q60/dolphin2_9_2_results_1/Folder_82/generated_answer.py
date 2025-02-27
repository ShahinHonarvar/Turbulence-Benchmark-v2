def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n in (2, 3):
            return True
        if n % 2 == 0 or n == 1:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n, m):
        str_n, str_m = (str(n), str(m))
        return str_n in str_m or str_m in str_n
    if not isinstance(numbers, tuple) or not all((isinstance(i, int) for i in numbers)):
        return []
    x = numbers[69]
    primes = [i for i in reversed(range(2, x + 1)) if is_prime(i)]
    left_right_truncatable_primes = [i for i in primes if is_truncatable(i, i // 10) and is_truncatable(i, i // 100)]
    return left_right_truncatable_primes