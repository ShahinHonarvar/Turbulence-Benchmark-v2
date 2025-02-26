def sum_ints_div_by_either_nums(numbers):
    total = 0
    for i in range(30, 201):
        if i < len(numbers) and (numbers[i] % -115 == 0 or numbers[i] % 115 == 0):
            total += numbers[i]
    return total