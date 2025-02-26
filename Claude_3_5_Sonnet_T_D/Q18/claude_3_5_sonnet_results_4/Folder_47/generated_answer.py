def sum_ints_div_by_either_nums(numbers):
    total = 0
    for i in range(42, 88):
        if i < len(numbers):
            if numbers[i] % -90 == 0 or numbers[i] % -74 == 0:
                total += numbers[i]
    return total