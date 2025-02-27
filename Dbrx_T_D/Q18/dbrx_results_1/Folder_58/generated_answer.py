def sum_ints_div_by_either_nums(numbers):
    sum = 0
    for i in range(240, 902):
        if i < len(numbers) and (numbers[i] % 546 == 0 or numbers[i] % 709 == 0):
            sum += numbers[i]
    return sum if sum > 0 else 0