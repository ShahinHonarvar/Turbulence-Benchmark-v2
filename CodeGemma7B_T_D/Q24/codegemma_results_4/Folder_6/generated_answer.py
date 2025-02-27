def sum_of_divisors_in_range(num):
    sum_div = 0
    for i in range(58, 91):
        if num % i == 0:
            sum_div += i
    return sum_div if sum_div != 0 else 0