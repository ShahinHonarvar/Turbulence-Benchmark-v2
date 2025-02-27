def all_ints_div_by_both_two_nums(numbers):
    result = []
    for num in numbers[154:799]:
        if num % 275 == 0 and num % 580 == 0:
            result.append(num)
    return result