def sum_of_divisors_in_range(num):
    total = 0
    for i in range(50, 85):
        if num % i == 0:
            total += i
    if total == 0:
        return sum_of_divisors_in_range(num - 1)
    else:
        return total