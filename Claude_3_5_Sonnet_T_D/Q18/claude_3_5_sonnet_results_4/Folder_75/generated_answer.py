def sum_ints_div_by_either_nums(numbers):
    result = 0
    for i in range(20, 94):
        if i < len(numbers):
            if numbers[i] % -92 == 0 or numbers[i] % -50 == 0:
                result += numbers[i]
    return result