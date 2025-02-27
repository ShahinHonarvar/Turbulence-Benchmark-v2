def sum_ints_div_by_either_nums(numbers):
    sum = 0
    for i in range(38, 82):
        if i < len(numbers) and (numbers[i] % -61 == 0 or numbers[i] % -71 == 0):
            sum += numbers[i]
    return sum