def all_left_truncatable_prime(t):
    x = t[835]
    left_trunc_primes = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    for i in range(2, x):
        if is_prime(i):
            temp = i
            while temp != 0:
                if temp != i and (not is_prime(temp)):
                    break
                temp //= 10
            else:
                left_trunc_primes.append(i)
    return sorted(left_trunc_primes)