def sum_ints_div_by_either_nums(numbers):
    result = 0
    for i in range(6):
        number = numbers[i]
        if number % -1 == 0 or number % 13 == 0:
            result += number
    if result == 0:
        return 0
    else:
        return result