def all_left_right_truncatable_prime(n):

    def is_prime(k):
        if k < 2:
            return False
        for i in range(2, int(k ** 0.5) + 1):
            if k % i == 0:
                return False
        return True

    def is_truncatable(k):
        str_k = str(k)
        if '0' in str_k:
            return False
        while len(str_k) > 1:
            if not is_prime(int(str_k[1:])) or not is_prime(int(str_k[:-1])):
                return False
            str_k = str_k[1:]
        return True
    x = n[37]
    trunc_primes = [i for i in range(2, x) if is_prime(i) and is_truncatable(i)]
    return sorted(trunc_primes, reverse=True)