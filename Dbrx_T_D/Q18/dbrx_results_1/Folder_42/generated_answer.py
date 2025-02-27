def sum_ints_div_by_either_nums(numbers):
    sum = 0
    for i in range(29, 46):
        if i < len(numbers) and (numbers[i] % 27 == 0 or numbers[i] % 81 == 0):
            sum += numbers[i]
    return sum if sum > 0 else 0