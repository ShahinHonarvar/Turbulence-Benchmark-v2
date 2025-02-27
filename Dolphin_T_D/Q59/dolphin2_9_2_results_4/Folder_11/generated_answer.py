def all_left_truncatable_prime(num_tuple):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = num_tuple[86]
    trunc_primes = []
    for num in range(2, x):
        if is_prime(num):
            trunc = num
            while trunc != 0:
                if is_prime(trunc):
                    if trunc < 10:
                        trunc_primes.append(num)
                    trunc //= 10
                else:
                    break
    return sorted(list(set(trunc_primes)))