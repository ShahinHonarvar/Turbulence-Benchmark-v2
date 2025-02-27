def sum_ints_div_by_either_nums(numbers):
    if len(numbers) < 10:
        return 0
    sum = 0
    for i in range(6, 10):
        if numbers[i] % -1 == 0 or numbers[i] % -10 == 0:
            sum += numbers[i]
    return sum