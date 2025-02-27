def sum_of_divisors_in_range(num):
    sum_num = 0
    for i in range(48, 63):
        if num % i == 0:
            sum_num += i
    return sum_num