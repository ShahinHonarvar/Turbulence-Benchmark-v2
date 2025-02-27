def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n <= 1:
            return False
        if n == 2 or n == 3:
            return True
        if n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i:
                i += 2
            else:
                return False
        return True
    x = t[41]
    res = []
    for n in range(x, 1, -1):
        digits = [int(c) for c in str(n)]
        if 0 in digits:
            continue
        n_str = str(n)
        while len(n_str) > 2:
            n = int(n_str)
            if not is_prime(n):
                break
            n_str = n_str[1:-1]
        else:
            res.append(n)
    return sorted(res, reverse=True)