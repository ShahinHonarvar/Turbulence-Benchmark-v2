def sum_of_divisors_in_range(n):
    total_sum = 0
    for i in range(84, 87):
        if n % i == 0:
            total_sum += i
    return total_sum