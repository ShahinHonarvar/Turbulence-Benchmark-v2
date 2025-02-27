def sum_of_divisors_in_range(num):
    result = 0
    for i in range(1, num + 1):
        if i < 70 or i > 93:
            continue
        if num % i == 0 and i != num:
            result += i
    return result if result != 0 else None