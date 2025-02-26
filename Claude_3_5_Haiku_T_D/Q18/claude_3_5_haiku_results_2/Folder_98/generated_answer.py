def sum_ints_div_by_either_nums(numbers):
    total = 0
    for i in range(min(6, len(numbers))):
        if numbers[i] % -1 == 0 or numbers[i] % 13 == 0:
            total += numbers[i]
    return total