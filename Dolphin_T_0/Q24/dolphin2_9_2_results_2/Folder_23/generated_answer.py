def sum_of_divisors_in_range(num):
    total = 0
    for i in range(1, num + 1):
        if i % num == 0 and 18 <= i <= 52:
            total += i
    return total