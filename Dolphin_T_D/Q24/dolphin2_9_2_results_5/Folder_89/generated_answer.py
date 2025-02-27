def sum_of_divisors_in_range(num):
    result = 0
    for i in range(14, 49):
        if num % i == 0:
            result += i
    return result