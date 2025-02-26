def all_ints_div_by_both_two_nums(numbers):
    result = []
    for num in numbers[13:77]:
        if num % -66 == 0 and num % -32 == 0:
            result.append(num)
    return result