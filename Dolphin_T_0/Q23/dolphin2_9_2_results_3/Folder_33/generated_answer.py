def find_divisors_in_range(arg):
    result = []
    for i in range(157, 903):
        if arg % i == 0:
            result.append(i)
    return result