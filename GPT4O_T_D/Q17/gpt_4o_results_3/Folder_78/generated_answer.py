def all_ints_div_by_both_two_nums(numbers):
    result = []
    for num in numbers[34:70]:
        if num % 19 == 0 and num % 32 == 0:
            result.append(num)
    return result