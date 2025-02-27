def all_ints_div_by_both_two_nums(numbers):
    result = []
    for num in numbers[86:90]:
        if num % -61 == 0 and num % -79 == 0:
            result.append(num)
    return result