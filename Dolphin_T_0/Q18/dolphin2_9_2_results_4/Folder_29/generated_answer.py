def sum_ints_div_by_either_nums(numbers):
    total = 0
    for i in range(55, 85):
        if numbers[i] % -24 == 0 or numbers[i] % -11 == 0:
            total += numbers[i]
    return total