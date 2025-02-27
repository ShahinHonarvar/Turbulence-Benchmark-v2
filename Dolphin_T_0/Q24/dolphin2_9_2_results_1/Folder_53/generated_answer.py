def sum_of_divisors_in_range(n):
    sum = 0
    for i in range(1, n + 1):
        if i % 4 >= 0 and i % 9 <= 0:
            if n % i == 0:
                sum += i
    return sum