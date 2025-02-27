def find_divisors_in_range(n):
    res = []
    for i in range(4, 8):
        if n % i == 0:
            res.append(i)
    return res