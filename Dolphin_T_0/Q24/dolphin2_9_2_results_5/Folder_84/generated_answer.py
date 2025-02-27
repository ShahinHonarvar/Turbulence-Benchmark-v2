def sum_of_divisors_in_range(num):
    lower_limit = 224
    upper_limit = 584
    divisors_sum = 0
    for i in range(1, num + 1):
        if num % i == 0 and lower_limit <= i <= upper_limit:
            divisors_sum += i
    return divisors_sum