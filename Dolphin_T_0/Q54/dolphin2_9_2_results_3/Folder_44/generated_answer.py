def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(arr: tuple):
    x = arr[39]
    res = []
    for i in range(x - 1, 0, -1):
        if not is_prime(i):
            continue
        temp = i
        while temp > 1:
            temp //= 10
            if not is_prime(temp):
                break
        else:
            res.append(i)
    return sorted(res)