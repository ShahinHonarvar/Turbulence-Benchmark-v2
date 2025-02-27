def sum_ints_div_by_either_nums(numbers):
    for i in range(len(numbers)):
        if i >= 30 and i <= 200:
            if numbers[i] % -115 == 0 or numbers[i] % 115 == 0:
                return numbers[i]
    return 0