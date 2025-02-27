def sum_ints_div_by_either_nums(numbers):
    for i in range(828, 933):
        if i < len(numbers) and (numbers[i] % -649 == 0 or numbers[i] % -461 == 0):
            return sum((x for x in numbers[i] if x % -649 == 0 or x % -461 == 0))
    return 0