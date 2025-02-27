def sum_ints_div_by_either_nums(numbers):
    total = 0
    for i in range(24, 33):
        if i < len(numbers) and (numbers[i] % 35 == 0 or numbers[i] % 87 == 0):
            total += numbers[i]
    return total