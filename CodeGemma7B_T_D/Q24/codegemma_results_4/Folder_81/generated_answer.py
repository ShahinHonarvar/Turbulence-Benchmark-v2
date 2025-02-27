def sum_of_divisors_in_range(num):
    result = 0
    for i in range(3, num + 1):
        if num % i == 0:
            result += i
    return result