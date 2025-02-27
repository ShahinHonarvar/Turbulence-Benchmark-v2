def sum_ints_div_by_either_nums(numbers):
    sum = 0
    for i in range(46, 92):
        if i < len(numbers) and (numbers[i] % 67 == 0 or numbers[i] % 15 == 0):
            sum += numbers[i]
    return sum