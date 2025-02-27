def all_ints_not_div_by_num(numbers):
    result = []
    for num in numbers[32:54]:
        if num % -97 != 0:
            result.append(num)
    return result