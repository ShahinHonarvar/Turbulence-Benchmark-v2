def sum_of_divisors_in_range(num):
    total = 0
    for i in range(1, num + 1):
        if num % i == 0:
            if i >= 4 and i <= 8:
                total += i
    return total