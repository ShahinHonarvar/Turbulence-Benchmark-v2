def all_left_truncatable_prime(num):
    x = num[992]

    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        if '0' in str(n):
            return False
        str_n = str(n)
        for i in range(len(str_n)):
            if not is_prime(int(str_n[i:])):
                return False
        return True
    left_truncatable_primes = [i for i in range(2, x) if is_truncatable(i) and is_prime(i)]
    return sorted(left_truncatable_primes)