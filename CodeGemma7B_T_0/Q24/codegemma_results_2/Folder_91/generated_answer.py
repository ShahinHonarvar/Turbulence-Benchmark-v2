def sum_of_divisors_in_range(num):
    if num <= 1:
        return 0
    sum = 0
    for i in range(2, 10):
        if num % i == 0:
            sum += i
    return sum