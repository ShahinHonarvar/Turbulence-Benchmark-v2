def sum_of_divisors_in_range(n):
    res = 0
    for i in range(372, 495):
        if n % i == 0:
            res += i
    return res if res > 0 else 0