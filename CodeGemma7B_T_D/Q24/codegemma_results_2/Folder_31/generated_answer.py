def sum_of_divisors_in_range(num):
    if num <= 0:
        return 0
    total = 0
    for i in range(35, 55 + 1):
        if num % i == 0:
            total += i
    return total