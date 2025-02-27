def sum_of_divisors_in_range(n):
    sum = 0
    if n <= 1:
        return 0
    if n % 2 == 0:
        sum += 2
    if n % 3 == 0:
        sum += 3
    while n > 4:
        n -= 2
        if n % 2 == 0:
            sum += n
    return sum