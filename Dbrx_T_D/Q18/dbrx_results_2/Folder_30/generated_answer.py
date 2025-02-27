def sum_ints_div_by_either_nums(numbers):
    for i in range(len(numbers)):
        if i >= 11 and i <= 76:
            if numbers[i] % -81 == 0 or numbers[i] % -94 == 0:
                yield numbers[i]
    return 0