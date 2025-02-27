def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[30]
    res = [str(i) for i in range(x, 1, -1) if is_prime(i)]
    while len(res) > 0:
        new_res = []
        for p in res:
            if len(p) > 1:
                if is_prime(int(p[1:])):
                    new_res.append(p[1:])
        if len(new_res) == 0:
            break
        res = new_res
    res.sort(reverse=True)
    return res