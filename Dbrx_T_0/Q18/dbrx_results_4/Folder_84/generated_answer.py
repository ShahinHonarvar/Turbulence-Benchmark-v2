def sum_ints_div_by_either_nums(numbers):
    sum = 0
    for i in range(78, 82):
        if i < len(numbers) and (numbers[i] % 76 == 0 or numbers[i] % 60 == 0):
            sum += numbers[i]
    return sum if sum > 0 else 0