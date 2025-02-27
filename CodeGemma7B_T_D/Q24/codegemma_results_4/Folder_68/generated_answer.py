def sum_of_divisors_in_range(num):
    sum = 0
    for n in range(3, 6 + 1):
        if num % n == 0:
            sum += n
    if sum == 0:
        return 0
    else:
        return sum