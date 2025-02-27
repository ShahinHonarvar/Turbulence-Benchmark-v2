def sum_of_divisors_in_range(n):
    sum_of_divisors = 0
    for i in range(84, 87):
        if i % n == 0:
            sum_of_divisors += i
    return sum_of_divisors