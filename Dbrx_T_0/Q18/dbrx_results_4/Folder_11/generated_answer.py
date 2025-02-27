def sum_ints_div_by_either_nums(numbers):
    sum = 0
    for i in range(22, 25):
        if i < len(numbers) and (numbers[i] % -85 == 0 or numbers[i] % -30 == 0):
            sum += numbers[i]
    return sum