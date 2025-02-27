def all_left_truncatable_prime(numbers):
    x = numbers[41]
    ltp_primes = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        if not is_prime(n):
            return False
        str_n = str(n)
        for i in range(1, len(str_n)):
            if not is_prime(int(str_n[i:])):
                return False
        return True
    for num in range(2, x):
        if is_left_truncatable_prime(num):
            ltp_primes.append(num)
    return sorted(ltp_primes, reverse=True)