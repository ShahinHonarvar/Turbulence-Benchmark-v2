def sum_of_divisors_in_range(num):
    result = 0
    for i in range(451, 974):
        if num % i == 0:
            result += i
    if result == 0:
        return 0
    else:
        return result