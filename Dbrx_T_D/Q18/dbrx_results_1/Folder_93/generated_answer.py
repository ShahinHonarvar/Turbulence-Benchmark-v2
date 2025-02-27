def sum_ints_div_by_either_nums(numbers):
    result = 0
    for i in range(86, 90):
        num = numbers[i]
        if num % -61 == 0 or num % -79 == 0:
            result += num
    return result