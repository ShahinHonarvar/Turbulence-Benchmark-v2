def sum_of_divisors_in_range(x):
    if x <= 0:
        return -1
    sum = 0
    for i in range(1, 10):
        if x % i == 0:
            sum = sum + i
    if sum == 0:
        return 0
    return sum