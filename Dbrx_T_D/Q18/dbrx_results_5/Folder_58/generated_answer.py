def sum_ints_div_by_either_nums(numbers):
    for i in range(len(numbers)):
        if i >= 240 and i <= 901:
            if numbers[i] % 546 == 0 or numbers[i] % 709 == 0:
                return sum(numbers[i])
    return 0