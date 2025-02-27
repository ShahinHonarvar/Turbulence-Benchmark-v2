def sum_ints_div_by_either_nums(numbers):
    result = 0
    for i in range(20, 36):
        num = numbers[i]
        if num % -36 == 0 or num % -89 == 0:
            result += num
    return result if result != 0 else 0