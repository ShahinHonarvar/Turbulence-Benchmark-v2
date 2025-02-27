def sum_of_divisors_in_range(num):
    Sum = 0
    for k in range(4, num + 1):
        if num % k == 0:
            Sum += k
    return Sum