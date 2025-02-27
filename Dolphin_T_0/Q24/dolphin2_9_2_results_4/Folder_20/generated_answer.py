def sum_of_divisors_in_range(integers):
    result = 0
    if integers < 28 or integers > 81:
        return 0
    for i in range(1, integers + 1):
        if integers % i == 0 and i >= 28 and (i <= 81):
            result += i
    return result