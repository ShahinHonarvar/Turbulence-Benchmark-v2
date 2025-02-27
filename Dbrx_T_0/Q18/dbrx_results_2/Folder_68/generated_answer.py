def sum_ints_div_by_either_nums(numbers):
    total = 0
    for i in range(7, len(numbers)):
        if numbers[i] % 5 == 0 or numbers[i] % 7 == 0:
            total += numbers[i]
    return total