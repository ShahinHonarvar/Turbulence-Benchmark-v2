def sum_of_divisors_in_range(num):
    if num <= 0:
        return 0
    sum = 0
    for i in range(378, 783):
        if num % i == 0:
            sum += i
    return sum