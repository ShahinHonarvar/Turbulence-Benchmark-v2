def sum_ints_div_by_either_nums(numbers):
    sum_divisible = 0
    for i in range(78, 82):
        if i < len(numbers) and (numbers[i] % 76 == 0 or numbers[i] % 60 == 0):
            sum_divisible += numbers[i]
    return sum_divisible