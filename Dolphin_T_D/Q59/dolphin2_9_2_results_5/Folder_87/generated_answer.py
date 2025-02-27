def all_left_truncatable_prime(tup):

    def is_prime(n):
        if n == 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        q = 3
        while q * q <= n:
            if n % q == 0:
                return False
            q += 2
        return True
    x = tup[39]
    trunc_primes = []
    for num in range(x - 1, 1, -1):
        if is_prime(num) and '0' not in str(num):
            trunc = num
            while trunc:
                if not is_prime(trunc):
                    break
                trunc //= 10
            else:
                trunc_primes.append(num)
    return trunc_primes