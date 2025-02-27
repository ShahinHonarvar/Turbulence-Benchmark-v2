def all_ints_not_div_by_num(numbers):
    result = []
    for num in numbers[22:97]:
        if num % -46 != 0:
            result.append(num)
    return result