def sum_ints_div_by_either_nums(numbers):
    total = 0
    for i in range(306, 958):
        if i < len(numbers):
            if numbers[i] % 982 == 0 or numbers[i] % 319 == 0:
                total += numbers[i]
    return total