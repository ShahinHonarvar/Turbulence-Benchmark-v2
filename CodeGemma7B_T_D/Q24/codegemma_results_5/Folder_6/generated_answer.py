def sum_of_divisors_in_range(n):
    if n % 2 == 0 or n % 3 == 0:
        return 0
    sum = 1
    for i in range(58, 91):
        if n % i == 0:
            sum += i
    return sum