def all_left_right_truncatable_prime(arg):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = arg[84]
    res = []
    for i in range(x, 0, -1):
        if '0' in str(i):
            continue
        num = i
        while num > 0 and len(str(num)) > 1:
            if not is_prime(num):
                break
            num = int(''.join([str(num)[1:-1] if len(str(num)) > 2 else '' for _ in range(len(str(num)) - 2)]) or str(num)[-1] + str(num)[0])
        if num > 0 and len(str(num)) > 0:
            res.append(i)
    return sorted(res, reverse=True)