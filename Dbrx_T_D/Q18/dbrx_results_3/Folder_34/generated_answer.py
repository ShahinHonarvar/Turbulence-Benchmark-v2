def sum_ints_div_by_either_nums(numbers):
    total = 0
    for i in range(len(numbers)):
        if i < 60 or i > 200:
            continue
        if numbers[i] % 9 == 0 or numbers[i] % 11 == 0:
            total += numbers[i]
    return total