def all_left_truncatable_prime(t):

    def is_prime(n):
        if n == 2 or n == 3:
            return True
        if n % 2 == 0 or n == 1:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    x = t[49]
    l = []
    for n in range(2, x):
        if is_prime(n) and '0' not in str(n):
            m = n
            while m:
                if not is_prime(m):
                    l.remove(n)
                    break
                m //= 10
            else:
                l.append(n)
    return sorted(l)