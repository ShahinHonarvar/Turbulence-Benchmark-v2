def sum_of_divisors_in_range(n):
    res = 0
    for i in range(11, 57):
        if n % i == 0:
            res += i
    return res