def sum_ints_div_by_either_nums(numbers):
    result = 0
    for i in range(1, 9):
        if i < len(numbers):
            if numbers[i] % -9 == 0 or numbers[i] % -3 == 0:
                result += numbers[i]
    return result