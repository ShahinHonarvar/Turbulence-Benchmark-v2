def sum_of_divisors_in_range(num):
    if not isinstance(num, int) or num <= 0:
        return 0
    total = 0
    for i in range(5, 10):
        if num % i == 0:
            total += i
    return total