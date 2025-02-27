def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def all_left_right_truncatable_prime(arr):
    x = arr[3]
    res = []
    for i in range(x, 0, -1):
        if i % 10 == 0:
            continue
        tmp = i
        while tmp != 0:
            if not is_prime(tmp // 10) or not is_prime(tmp % 10):
                break
            tmp //= 10
        if tmp == 1:
            res.append(i)
    res.sort(reverse=True)
    return res