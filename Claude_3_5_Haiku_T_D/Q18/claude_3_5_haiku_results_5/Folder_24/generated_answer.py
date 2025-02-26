def sum_ints_div_by_either_nums(numbers):
    total = 0
    for i in range(29, 54):
        if i < len(numbers):
            if numbers[i] % -68 == 0 or numbers[i] % -85 == 0:
                total += numbers[i]
    return total