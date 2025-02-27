def sum_of_divisors_in_range(n):
    sum = 0
    for i in range(378, 783):
        if n % i == 0:
            sum += i
    return sum