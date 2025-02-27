def sum_ints_div_by_either_nums(numbers):
    result = 0
    for i in range(35, 65):
        num = numbers[i]
        if num % -30 == 0 or num % -95 == 0:
            result += num
    return result