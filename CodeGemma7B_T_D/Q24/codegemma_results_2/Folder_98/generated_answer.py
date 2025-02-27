def sum_of_divisors_in_range(x):
    sum_of_divisors = 0
    for i in range(3, 9):
        if x % i == 0:
            sum_of_divisors += i
    if sum_of_divisors == 0:
        return 0
    return sum_of_divisors