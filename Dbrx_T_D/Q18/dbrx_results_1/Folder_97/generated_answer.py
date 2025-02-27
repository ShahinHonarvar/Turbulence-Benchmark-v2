def sum_ints_div_by_either_nums(numbers):
    sum = 0
    for i in range(58, 76):
        if i < len(numbers) and (numbers[i] % 72 == 0 or numbers[i] % 62 == 0):
            sum += numbers[i]
    return sum