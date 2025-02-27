def sum_of_divisors_in_range(n):
    sum = 0
    for i in range(35, 99):
        if i % n == 0:
            sum += i
    if sum == 0:
        return 0
    else:
        return sum