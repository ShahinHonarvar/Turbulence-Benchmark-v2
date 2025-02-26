def sum_ints_div_by_either_nums(numbers):
    total = 0
    for i in range(86, 91):
        if numbers[i] % -71 == 0 or numbers[i] % -67 == 0:
            total += numbers[i]
    return total