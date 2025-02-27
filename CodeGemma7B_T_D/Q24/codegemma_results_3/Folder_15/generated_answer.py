def sum_of_divisors_in_range(num):
    sum = 0
    for i in range(7, 10):
        if num % i == 0:
            sum += i
    if sum == 0:
        return 0
    else:
        return sum