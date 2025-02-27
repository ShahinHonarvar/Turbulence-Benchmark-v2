def sum_of_divisors_in_range(num):
    if num <= 48:
        return 0
    elif num >= 60:
        return 0
    else:
        sum_of_divisors = 0
        for i in range(49, 61):
            if num % i == 0:
                sum_of_divisors += i
        return sum_of_divisors