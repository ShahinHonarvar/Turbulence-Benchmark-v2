def sum_ints_div_by_either_nums(numbers):
    sum = 0
    for i in range(58, 82):
        if i < len(numbers) and (numbers[i] % 55 == 0 or numbers[i] % 10 == 0):
            sum += numbers[i]
    return sum