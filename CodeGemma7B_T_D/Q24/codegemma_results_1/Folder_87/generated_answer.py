def sum_of_divisors_in_range(num):
    if num < 1:
        return 0
    total = 0
    for i in range(50, 82):
        if num % i == 0:
            total += i
    if total == 0:
        return 0
    return total