def all_ints_not_div_by_num(numbers):
    result = []
    for number in numbers[25:45]:
        if number % -72 != 0:
            result.append(number)
    return result