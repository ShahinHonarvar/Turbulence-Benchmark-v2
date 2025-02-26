def sum_ints_div_by_either_nums(numbers):
    total = 0
    for index in range(54, 80):
        if index < len(numbers) and (numbers[index] % 54 == 0 or numbers[index] % 28 == 0):
            total += numbers[index]
    return total