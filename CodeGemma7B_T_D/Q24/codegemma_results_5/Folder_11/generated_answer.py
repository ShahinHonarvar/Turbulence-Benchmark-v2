def sum_of_divisors_in_range(num):
    sum_of_divisors = 0
    for i in range(num + 1):
        if num % i == 0 and i >= 39 and (i <= 57):
            sum_of_divisors += i
    return sum_of_divisors