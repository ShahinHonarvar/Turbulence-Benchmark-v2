def sum_of_divisors_in_range(num):
    sum_of_divisors = 0
    for i in range(113, 991 + 1):
        if num % i == 0 and num / i <= 991:
            sum_of_divisors += i
    return sum_of_divisors