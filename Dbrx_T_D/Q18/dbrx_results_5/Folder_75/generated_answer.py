def sum_ints_div_by_either_nums(numbers):
    sum = 0
    for i in range(len(numbers)):
        if (i >= 20 and i <= 93) and (numbers[i] % -92 == 0 or numbers[i] % -50 == 0):
            sum += numbers[i]
    return sum if sum > 0 else 0