def sum_ints_div_by_either_nums(numbers):
    total = 0
    for i in range(42, 44):
        if i < len(numbers) and (numbers[i] % 15 == 0 or numbers[i] % 87 == 0):
            total += numbers[i]
    return total