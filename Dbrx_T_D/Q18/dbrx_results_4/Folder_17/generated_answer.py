def sum_ints_div_by_either_nums(numbers):
    total = 0
    for i in range(81, 90):
        if i < len(numbers) and (numbers[i] % 56 == 0 or numbers[i] % 68 == 0):
            total += numbers[i]
    return total