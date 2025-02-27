def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(params):
    x = params[0]
    res = []
    for i in range(x, 1, -1):
        if '0' in str(i):
            continue
        trunc = i
        while trunc > 9:
            trunc = int(str(trunc)[1:-1])
            if not is_prime(trunc):
                break
        if trunc in [2, 3, 5, 7] and is_prime(i):
            res.append(i)
    return res