def sum_ints_div_by_either_nums(numbers):
    total = 0
    for i in range(13, 77):
        if i < len(numbers) and (numbers[i] % -66 == 0 or numbers[i] % -32 == 0):
            total += numbers[i]
    return total