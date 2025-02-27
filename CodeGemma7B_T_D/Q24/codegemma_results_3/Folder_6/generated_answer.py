def sum_of_divisors_in_range(num):
    if num <= 1:
        return 0
    sum = 0
    i = 58
    while i <= 90:
        if num % i == 0:
            sum += i
        i += 1
    return sum