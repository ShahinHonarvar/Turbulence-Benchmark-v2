def all_left_truncatable_prime(num_tuple):
    x = num_tuple[36]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        sn = str(n)
        for i in range(len(sn)):
            if not is_prime(int(sn[i:])):
                return False
        return True
    left_truncatable_primes = [i for i in range(2, x) if is_prime(i) and is_truncatable(i)]
    return sorted(left_truncatable_primes)