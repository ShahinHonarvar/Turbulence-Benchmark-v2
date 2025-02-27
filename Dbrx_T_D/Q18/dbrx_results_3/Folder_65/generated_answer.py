def sum_ints_div_by_either_nums(numbers):
    for i in range(50, 93):
        if i < len(numbers) and (numbers[i] % -94 == 0 or numbers[i] % -95 == 0):
            return sum((x for x in numbers[50:93] if x % -94 == 0 or x % -95 == 0))
    return 0