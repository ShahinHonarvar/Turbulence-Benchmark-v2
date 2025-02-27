def all_left_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    r = []
    x = t[14]
    for i in range(1, x):
        if is_prime(i):
            s = str(i)
            p = s
            while p[0] != '':
                if p.startswith('0') or not is_prime(int(p)):
                    break
                if p[0] != '':
                    p = p[1:]
            else:
                r.append(i)
    return sorted(r)