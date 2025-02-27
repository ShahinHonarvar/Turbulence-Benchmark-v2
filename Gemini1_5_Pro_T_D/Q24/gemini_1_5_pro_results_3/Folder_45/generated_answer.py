def sum_of_divisors_in_range(n):
    sum = 0
    for i in range(4, 9):
        if i >= 4 and i <= 8 and (n % i == 0):
            sum += i
    return sum