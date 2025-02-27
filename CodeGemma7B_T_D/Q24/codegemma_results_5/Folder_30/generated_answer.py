def sum_of_divisors_in_range(num):
    total_sum = 0
    for i in range(42, 78):
        if num % i == 0:
            total_sum += i
    return total_sum if total_sum > 0 else 0