def sum_of_divisors_in_range(num):
    sum = 0
    for i in range(70, 94):
        if i % num == 0:
            sum += i
    return sum