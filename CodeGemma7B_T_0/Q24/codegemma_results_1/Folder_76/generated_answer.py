def sum_of_divisors_in_range(num):
    sum = 0
    for i in range(744, 886):
        if num % i == 0:
            sum += i
    return sum