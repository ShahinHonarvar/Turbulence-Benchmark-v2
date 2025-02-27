def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[41]
    res = [i for i in range(2, x + 1) if is_prime(i)]
    for i in range(len(res) - 1, 0, -1):
        if res[i] % 10 == 0 or not is_prime(res[i] // 10):
            res = res[:i]
    for b in range(2, 9):
        tmp = [str(b)]
        for num in res:
            if str(num)[-1] == str(b):
                tmp.append(str(num)[1:-1])
        for el in tmp[::-1]:
            if el not in res:
                tmp = tmp[:-1]
        res = [int(''.join(a)) for a in zip(tmp, res * len(tmp)) if is_prime(int(''.join(a)))]
    return sorted(res)