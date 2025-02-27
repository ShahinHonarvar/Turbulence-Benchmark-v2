def all_left_truncatable_prime(numbers):
    if len(numbers) <= 992:
        return []
    x = numbers[992]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        while str_n:
            if not is_prime(int(str_n)):
                return False
            str_n = str_n[1:]
        return True
    truncatable_primes = [n for n in range(2, x) if is_left_truncatable_prime(n)]
    return truncatable_primes