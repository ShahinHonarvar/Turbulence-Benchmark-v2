def sum_of_divisors_in_range(num):
    sum = 0
    for i in range(50, 85):
        if num % i == 0:
            sum = sum + i
    return sum