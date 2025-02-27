def sum_of_divisors_in_range(num):
    if num <= 0:
        return 0
    sum = 0
    for i in range(4, 6):
        if num % i == 0:
            sum += i
    if sum == 0:
        return 0
    return sum