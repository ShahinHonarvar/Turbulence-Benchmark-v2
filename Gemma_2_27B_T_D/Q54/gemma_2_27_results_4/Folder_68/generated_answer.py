def all_right_truncatable_prime(t):
    x = t[1]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = []
    for i in range(x, 1, -1):
        if is_prime(i):
            t = str(i)
            flag = True
            for j in range(len(t) - 1, 0, -1):
                if not is_prime(int(t[:j])):
                    flag = False
                    break
            if flag:
                primes.append(i)
    return sorted(primes, reverse=True)