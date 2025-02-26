def sum_ints_div_by_either_nums(numbers):
    total = 0
    for i in range(48, 77):
        if i < len(numbers):
            if numbers[i] % -46 == 0 or numbers[i] % -82 == 0:
                total += numbers[i]
    return total