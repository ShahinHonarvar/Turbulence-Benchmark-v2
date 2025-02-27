def all_left_right_truncatable_prime(n):
    x = n[767]

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def all_truncations(n):
        n = str(n)
        res = set()
        for i in range(len(n) - 1):
            res.add(''.join([n[i + j] for j in range(len(n) - i)]))
        return sorted(list(res), reverse=True)
    res = []
    for i in range(2, x + 1):
        if is_prime(i):
            if i < 10:
                res.append(i)
            elif all([is_prime(int(str(i).rstrip('0').rstrip(str(i[-1])))) for i in all_truncations(i)]):
                res.append(i)
    return res