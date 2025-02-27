def sum_of_divisors_in_range(int):
    sum = 0
    for i in range(224, 585):
        if int % i == 0:
            sum += i
    if sum == 0:
        return 0
    return sum