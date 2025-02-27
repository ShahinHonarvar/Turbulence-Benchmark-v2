def sum_ints_div_by_either_nums(numbers):
    total = 0
    for i in range(7, 10):
        if i < len(numbers) and (numbers[i] % 2 == 0 or numbers[i] % 3 == 0):
            total += numbers[i]
    return total