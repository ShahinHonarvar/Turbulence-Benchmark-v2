def sum_ints_div_by_either_nums(numbers):
    total = 0
    for i in range(len(numbers)):
        if (i >= 70 and i <= 200) and (numbers[i] % 3 == 0 or numbers[i] % -300 == 0):
            total += numbers[i]
    return total