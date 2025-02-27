def sum_ints_div_by_either_nums(numbers):
    sum = 0
    for i in range(77, 88):
        if i < len(numbers) and (numbers[i] % 23 == 0 or numbers[i] % 57 == 0):
            sum += numbers[i]
    return sum