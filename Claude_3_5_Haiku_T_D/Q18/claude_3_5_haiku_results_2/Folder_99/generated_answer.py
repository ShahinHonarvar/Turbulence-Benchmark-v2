def sum_ints_div_by_either_nums(numbers):
    total = 0
    for num in numbers[154:799]:
        if num % 275 == 0 or num % 580 == 0:
            total += num
    return total