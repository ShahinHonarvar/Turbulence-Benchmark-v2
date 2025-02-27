def sum_of_divisors_in_range(n):
    sum = 0
    for i in range(1, n + 1):
        if 70 <= i <= 72 and n % i == 0:
            sum += i
    return sum