def sum_of_divisors_in_range(x):
    result = 0
    for i in range(48, 63):
        if x % i == 0:
            result += i
    return result