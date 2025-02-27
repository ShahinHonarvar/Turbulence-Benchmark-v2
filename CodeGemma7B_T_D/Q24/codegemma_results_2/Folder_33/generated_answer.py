def sum_of_divisors_in_range(num):
    result = 0
    for i in range(157, 903):
        if i % num == 0:
            result += i
    if result == 0:
        return 0
    else:
        return result