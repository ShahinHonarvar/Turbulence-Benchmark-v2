def sum_ints_div_by_either_nums(numbers):
    sum = 0
    for i in range(8, 10):
        if i < len(numbers) and (numbers[i] % -3 == 0 or numbers[i] % 6 == 0):
            sum += numbers[i]
    return sum