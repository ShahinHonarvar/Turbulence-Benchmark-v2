def sum_ints_div_by_either_nums(numbers):
    total = 0
    for i in range(len(numbers)):
        if i >= 90 and i <= 97 and (numbers[i] % 13 == 0 or numbers[i] % 35 == 0):
            total += numbers[i]
    return total