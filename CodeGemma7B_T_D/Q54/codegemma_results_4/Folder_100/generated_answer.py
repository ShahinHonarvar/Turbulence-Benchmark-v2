def all_right_truncatable_prime(x: tuple) -> list:
    if x[26] in [1, 2, 3, 5, 7, 9]:
        res = []
        for i in range(10 ** (len(str(x[26])) - 1), x[26]):
            j = i
            while j != 0:
                if j in [1, 2, 3, 5, 7, 9]:
                    res.append(j)
                    break
                j //= 10
        return sorted(res)
    return []