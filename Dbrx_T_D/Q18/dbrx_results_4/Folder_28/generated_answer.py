def sum_ints_div_by_either_nums(numbers):
    total = 0
    for i in range(len(numbers)):
        if i >= 34 and i <= 81:
            if numbers[i] % 27 == 0 or numbers[i] % 57 == 0:
                total += numbers[i]
    return total