def sum_of_divisors_in_range(num):
    if num <= 1:
        return 0
    Sum = 0
    for i in range(2, 6):
        if num % i == 0:
            Sum += i
    return Sum