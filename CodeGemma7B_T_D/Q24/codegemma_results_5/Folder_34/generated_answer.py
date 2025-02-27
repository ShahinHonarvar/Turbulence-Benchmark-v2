def sum_of_divisors_in_range(a):
    sum = 0
    for i in range(4, 5 + 1):
        if a % i == 0:
            sum += i
    return sum