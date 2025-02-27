def sum_ints_div_by_either_nums(numbers):
    sum = 0
    for i in range(61, 89):
        if i < len(numbers) and (numbers[i] % 31 == 0 or numbers[i] % 11 == 0):
            sum += numbers[i]
    return sum if sum > 0 else 0