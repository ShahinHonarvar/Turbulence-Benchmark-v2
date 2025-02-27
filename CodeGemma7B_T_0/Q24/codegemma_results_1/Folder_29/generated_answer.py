def sum_of_divisors_in_range(num):
    if num <= 0:
        return 0
    sum = 0
    for i in range(43, 78):
        if num % i == 0:
            sum += i
    return sum