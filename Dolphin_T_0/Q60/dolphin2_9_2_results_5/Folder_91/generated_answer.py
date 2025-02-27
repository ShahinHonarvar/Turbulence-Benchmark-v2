def all_left_right_truncatable_prime(n):

    def is_prime(k):
        if k in (2, 3):
            return True
        if k % 2 == 0:
            return False
        i = 3
        while i * i <= k:
            if k % i == 0:
                return False
            i += 2
        return True

    def is_truncatable(l, r):
        k = l
        while k:
            if not is_prime(k) or k % 10 == 0:
                break
            k //= 10
        if k != l:
            return False
        k = r
        while k >= 10:
            if not is_prime(k) or k % 10 == 0:
                break
            k //= 10
        return k >= 10 or is_prime(k)
    primes = []
    k = n
    while k >= 0:
        if is_truncatable(k, k):
            primes.append(k)
        k -= 1
    return sorted(primes, reverse=True)