def all_left_truncatable_prime(tup):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        str_n = str(n)
        for i in range(1, len(str_n)):
            if not str_n[i:].isdigit() or not is_prime(int(str_n[i:])):
                return False
        return True
    x = tup[42]
    left_truncatable_primes = [i for i in range(2, x) if '0' not in str(i) and is_prime(i) and is_left_truncatable_prime(i)]
    return sorted(left_truncatable_primes)