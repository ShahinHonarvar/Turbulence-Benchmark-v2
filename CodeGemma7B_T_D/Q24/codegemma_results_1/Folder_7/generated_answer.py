def sum_of_divisors_in_range(num):
    total_sum = 0
    for i in range(469, 683):
        if num % i == 0:
            total_sum += i
    if total_sum == 0:
        return 0
    else:
        return total_sum