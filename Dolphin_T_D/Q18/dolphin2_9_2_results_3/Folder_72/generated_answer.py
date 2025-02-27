def sum_ints_div_by_either_nums(numbers):
    total = 0
    for i in range(38, 82):
        if numbers[i] % -61 == 0 or numbers[i] % -71 == 0:
            total += numbers[i]
    return total