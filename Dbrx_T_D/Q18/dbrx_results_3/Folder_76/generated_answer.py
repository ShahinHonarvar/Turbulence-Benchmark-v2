def sum_ints_div_by_either_nums(numbers):
    result = 0
    for i in range(250, 630):
        num = numbers[i]
        if num % 850 == 0 or num % 587 == 0:
            result += num
    return result