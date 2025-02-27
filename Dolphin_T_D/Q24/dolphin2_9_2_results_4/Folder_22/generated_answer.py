def sum_of_divisors_in_range(num):
    sum_divisors = 0
    for i in range(4, 8):
        if num % i == 0:
            sum_divisors += i
    if sum_divisors == 0:
        return 0
    else:
        return sum_divisors