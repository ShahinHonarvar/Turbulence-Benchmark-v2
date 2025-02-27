def sum_of_divisors_in_range(num):
    res = 0
    for i in range(4, 9):
        if num % i == 0:
            res += i
    return res