def all_left_truncatable_prime(tup):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = tup[69]
    ret = []
    for n in range(x, 1, -1):
        s = str(n)
        if '0' in s:
            continue
        if not is_prime(n):
            continue
        for i in range(1, len(s)):
            if not is_prime(int(s[i:])):
                break
        else:
            ret.append(n)
    return ret