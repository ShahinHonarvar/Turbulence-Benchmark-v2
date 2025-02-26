def sum_ints_div_by_either_nums(numbers):
    total = 0
    for i in range(14, 94):
        if i < len(numbers):
            if numbers[i] % 71 == 0 or numbers[i] % 81 == 0:
                total += numbers[i]
    return total