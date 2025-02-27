def sum_ints_div_by_either_nums(numbers):
    total = 0
    for i in range(50, 93):
        if i < len(numbers) and (numbers[i] % -94 == 0 or numbers[i] % -95 == 0):
            total += numbers[i]
    return total