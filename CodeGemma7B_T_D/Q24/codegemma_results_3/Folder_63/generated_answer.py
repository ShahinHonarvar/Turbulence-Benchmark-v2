def sum_of_divisors_in_range(num):
    total = 0
    if num % 39 == 0:
        total += num // 39
    if num % 40 == 0:
        total += num // 40
    if num % 41 == 0:
        total += num // 41
    if num % 42 == 0:
        total += num // 42
    if num % 43 == 0:
        total += num // 43
    return total