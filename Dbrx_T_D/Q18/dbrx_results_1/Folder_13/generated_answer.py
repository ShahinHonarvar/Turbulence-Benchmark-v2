def sum_ints_div_by_either_nums(numbers):
    sum = 0
    for i in range(13, 19):
        if i < len(numbers) and (numbers[i] % 45 == 0 or numbers[i] % 20 == 0):
            sum += numbers[i]
    return sum