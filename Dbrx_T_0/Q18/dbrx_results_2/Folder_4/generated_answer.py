def sum_ints_div_by_either_nums(numbers):
    for i in range(len(numbers)):
        if i < 86 or i > 90:
            continue
        if numbers[i] % -71 == 0 or numbers[i] % -67 == 0:
            return sum(numbers[86:91])
    return 0