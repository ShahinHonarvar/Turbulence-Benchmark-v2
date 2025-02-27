def sum_ints_div_by_either_nums(numbers):
    total = 0
    for i in range(len(numbers)):
        if i >= 0 and i <= 1:
            if numbers[i] % 2 == 0 or numbers[i] % 1 == 0:
                total += numbers[i]
    return total