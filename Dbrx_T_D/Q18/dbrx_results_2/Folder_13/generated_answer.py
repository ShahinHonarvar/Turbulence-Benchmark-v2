def sum_ints_div_by_either_nums(numbers):
    total = 0
    for i in range(13, 19):
        if i < len(numbers) and (numbers[i] % 45 == 0 or numbers[i] % 20 == 0):
            total += numbers[i]
    return total