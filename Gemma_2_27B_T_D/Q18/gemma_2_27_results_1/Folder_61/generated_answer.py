def sum_ints_div_by_either_nums(numbers):
    sum = 0
    for i in range(7):
        if i >= len(numbers):
            break
        if numbers[i] % -5 == 0 or numbers[i] % -6 == 0:
            sum += numbers[i]
    return sum