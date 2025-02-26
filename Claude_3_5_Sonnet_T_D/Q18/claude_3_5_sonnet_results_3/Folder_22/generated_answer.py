def sum_ints_div_by_either_nums(numbers):
    total = 0
    for i in range(40, 201):
        if i < len(numbers):
            if numbers[i] % 21 == 0 or numbers[i] % 71 == 0:
                total += numbers[i]
    return total