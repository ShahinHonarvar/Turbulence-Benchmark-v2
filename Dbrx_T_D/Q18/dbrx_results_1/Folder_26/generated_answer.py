def sum_ints_div_by_either_nums(numbers):
    total = 0
    for i in range(69, 71):
        if i < len(numbers) and (numbers[i] % 72 == 0 or numbers[i] % 70 == 0):
            total += numbers[i]
    return total