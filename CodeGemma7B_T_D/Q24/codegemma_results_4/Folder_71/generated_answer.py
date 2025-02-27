def sum_of_divisors_in_range(x):
    sum = 0
    for i in range(45, 73):
        if x % i == 0:
            sum += i
    if sum == 0:
        return 0
    else:
        return sum