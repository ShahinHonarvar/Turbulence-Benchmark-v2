def sum_ints_div_by_either_nums(numbers):
    sum = 0
    for i in range(25, 81):
        if numbers[i] % -20 == 0 or numbers[i] % -26 == 0:
            sum += numbers[i]
    return sum