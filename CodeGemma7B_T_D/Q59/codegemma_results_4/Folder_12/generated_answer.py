def all_left_truncatable_prime(x):
    x = x[70]
    ans = []

    def is_prime(s):
        if s in [0, 1]:
            return False
        for i in range(2, int(s ** 0.5) + 1):
            if s % i == 0:
                return False
        return True
    for i in range(0, x):
        s = str(i)
        if '0' in s:
            continue
        if is_prime(i) and is_prime(int(s[1:])):
            ans.append(i)
    return sorted(ans, reverse=True)