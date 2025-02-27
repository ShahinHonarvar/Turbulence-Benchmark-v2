def sum_ints_div_by_either_nums(numbers):
    total = 0
    for i in range(38, 53):
        if i < len(numbers) and (numbers[i] % -41 == 0 or numbers[i] % -47 == 0):
            total += numbers[i]
    return total