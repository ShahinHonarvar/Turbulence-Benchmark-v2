def sum_ints_div_by_either_nums(numbers):
    result = 0
    for i in range(max(46, len(numbers)) if len(numbers) < 91 else 91):
        if i >= 46 and (numbers[i] % 67 == 0 or numbers[i] % 15 == 0):
            result += numbers[i]
    return result if result > 0 else 0