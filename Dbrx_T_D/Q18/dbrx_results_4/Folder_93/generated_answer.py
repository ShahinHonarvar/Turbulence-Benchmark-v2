def sum_ints_div_by_either_nums(numbers):
    result = 0
    for i in range(86, 90):
        if i < len(numbers) and (numbers[i] % -61 == 0 or numbers[i] % -79 == 0):
            result += numbers[i]
    return result if result != 0 else 0