def all_left_truncatable_prime(arg):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = arg[86]
    left_trunc_primes = []
    for i in range(2, x):
        if '0' not in str(i) and len(i.__str__()) == i:
            left_trunc = i
            while left_trunc > 0:
                if not is_prime(left_trunc):
                    break
                left_trunc //= 10
            else:
                left_trunc_primes.append(i)
    return sorted(left_trunc_primes, reverse=True)