def sum_ints_div_by_either_nums(numbers):
    result = 0
    for i in range(len(numbers)):
        if i >= 58 and i <= 75:
            if numbers[i] % 72 == 0 or numbers[i] % 62 == 0:
                result += numbers[i]
    return result if result != 0 else 0