def sum_of_divisors_in_range(num):
    sum = 0
    for x in range(11, 42):
        if num % x == 0:
            sum += x
    return sum if sum > 0 else 0