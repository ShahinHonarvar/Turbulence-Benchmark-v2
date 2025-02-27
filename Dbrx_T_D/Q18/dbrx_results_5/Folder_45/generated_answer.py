def sum_ints_div_by_either_nums(numbers):
    result = 0
    for i in range(len(numbers)):
        if i < 30 or i > 200:
            continue
        if numbers[i] % -115 == 0 or numbers[i] % 115 == 0:
            result += numbers[i]
    return result