def sum_of_divisors_in_range(n):
    sum = 0
    for i in range(70, 73):
        if i % n == 0:
            sum += i
    return sum