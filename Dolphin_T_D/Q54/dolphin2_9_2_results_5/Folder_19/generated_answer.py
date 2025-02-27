def all_right_truncatable_prime(t):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    x = t[67]
    right_truncatable_primes = []
    for i in range(x - 1, 0, -1):
        if is_prime(i):
            j = i
            while j > 1:
                j //= 10
                if not is_prime(j):
                    break
            else:
                right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes, reverse=True)