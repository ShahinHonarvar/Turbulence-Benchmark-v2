def sum_ints_div_by_either_nums(numbers):
    total = 0
    for i in range(10, 80):
        if i < len(numbers) and (numbers[i] % -74 == 0 or numbers[i] % -58 == 0):
            total += numbers[i]
    return total