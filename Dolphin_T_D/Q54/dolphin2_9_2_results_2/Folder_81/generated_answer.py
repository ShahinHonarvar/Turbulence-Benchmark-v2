def all_right_truncatable_prime(lst):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = lst[98]
    res = []
    for num in range(x, 1, -1):
        r = str(num)
        if is_prime(num):
            for i in range(len(r) - 1):
                r = r[:-1]
                if not is_prime(int(r)):
                    break
                if r[::-1][i:] == r:
                    res.append(num)
    return sorted(res)