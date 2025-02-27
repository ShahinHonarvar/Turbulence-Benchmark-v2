def all_right_truncatable_prime(numbers):

    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = numbers[64]
    primes = [i for i in range(2, x) if is_prime(i)]

    def is_right_truncatable(n):
        str_n = str(n)
        for i in range(len(str_n) - 1):
            if not is_prime(int(str_n[i:])):
                return False
        return True
    right_truncatable_primes = [i for i in primes if is_right_truncatable(i)]
    return sorted(right_truncatable_primes, reverse=True)