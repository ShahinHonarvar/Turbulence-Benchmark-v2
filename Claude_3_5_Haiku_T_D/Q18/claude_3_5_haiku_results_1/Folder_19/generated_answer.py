def sum_ints_div_by_either_nums(numbers):
    total = 0
    for i in range(1, 5):
        if i < len(numbers):
            if numbers[i] % 4 == 0 or numbers[i] % -6 == 0:
                total += numbers[i]
    return total