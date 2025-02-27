def sum_of_divisors_in_range(num):
    if num <= 0:
        return 0
    result = 0
    for i in range(35, 56):
        if num % i == 0:
            result += i
    return result