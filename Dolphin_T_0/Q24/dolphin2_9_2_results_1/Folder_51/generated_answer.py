def sum_of_divisors_in_range(x):
    sum = 0
    for i in range(2, 8):
        if x % i == 0:
            sum += i
    return sum