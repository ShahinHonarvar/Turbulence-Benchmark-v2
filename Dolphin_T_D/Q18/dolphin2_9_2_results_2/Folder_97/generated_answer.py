def sum_ints_div_by_either_nums(numbers):
    result = 0
    for i in range(58, 76):
        if numbers[i] % 72 == 0 or numbers[i] % 62 == 0:
            result += numbers[i]
    return result