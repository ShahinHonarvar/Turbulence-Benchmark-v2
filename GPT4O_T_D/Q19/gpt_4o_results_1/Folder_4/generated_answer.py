def all_ints_not_div_by_num(numbers):
    result = []
    for number in numbers[20:49]:
        if number % 36 != 0:
            result.append(number)
    return result