def sum_of_divisors_in_range(num):
    total_sum = 0
    for i in range(70, 94):
        if num % i == 0:
            total_sum += i
    return total_sum