def sum_of_divisors_in_range(num):
    for i in range(228, 847):
        if num % i == 0:
            num += i
    return num