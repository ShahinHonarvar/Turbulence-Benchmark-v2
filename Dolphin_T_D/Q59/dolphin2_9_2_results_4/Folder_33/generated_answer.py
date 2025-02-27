def all_left_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[945]
    res = [i for i in range(x, 1, -1) if is_prime(i)]
    while res:
        t = str(res.pop())
        if '0' in t:
            continue
        for i in range(1, len(t)):
            if not is_prime(int(t[i:])):
                break
        else:
            res.append(int(t))
    return res