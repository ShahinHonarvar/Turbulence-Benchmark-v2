def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[84]
    primes = []
    for i in range(x, 0, -1):
        if '0' in str(i):
            continue
        if is_prime(i):
            truncated = i
            while truncated > 9:
                truncated //= 10
                if not is_prime(truncated):
                    break
            else:
                truncated = i
                while truncated > 9:
                    truncated %= 10
                    if not is_prime(truncated):
                        break
                else:
                    primes.append(i)
    return sorted(primes, reverse=True)