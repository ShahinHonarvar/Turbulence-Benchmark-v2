def sum_of_divisors_in_range(num):
    total = 0
    for i in range(70, 73):
        if num % i == 0:
            total += i
    if total == 0:
        return 0
    else:
        return total