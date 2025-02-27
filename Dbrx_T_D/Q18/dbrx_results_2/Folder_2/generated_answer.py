def sum_ints_div_by_either_nums(numbers):
    sum = 0
    for i in range(73, 87):
        if i < len(numbers) and (numbers[i] % 54 == 0 or numbers[i] % 82 == 0):
            sum += numbers[i]
    return sum