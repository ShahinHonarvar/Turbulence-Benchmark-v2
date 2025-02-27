def sum_ints_div_by_either_nums(numbers):
    sum = 0
    for i in range(93, 95):
        if i < len(numbers) and (numbers[i] % -53 == 0 or numbers[i] % -91 == 0):
            sum += numbers[i]
    return sum if sum != 0 else None