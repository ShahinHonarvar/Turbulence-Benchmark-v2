def sum_of_divisors_in_range(n):
    sum = 0
    for i in range(60, 87):
        if i <= n and n % i == 0:
            sum += i
    return sum