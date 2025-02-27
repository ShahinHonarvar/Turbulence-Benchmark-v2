def sum_ints_div_by_either_nums(numbers):
    total = 0
    for i in range(len(numbers)):
        if i >= 6 and i <= 9:
            if numbers[i] % -1 == 0 or numbers[i] % -10 == 0:
                total += numbers[i]
    return total