def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[54]
    res = []
    for i in range(x, 1, -1):
        if '0' in str(i) or not is_prime(i):
            continue
        while i > 1:
            if is_prime(i // 10) and is_prime(i % 10):
                i //= 10
            else:
                break
        if i == 1:
            res.append(i)
    return res