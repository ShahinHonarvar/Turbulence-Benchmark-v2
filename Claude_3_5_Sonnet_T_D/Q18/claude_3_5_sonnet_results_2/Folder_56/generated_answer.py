def sum_ints_div_by_either_nums(numbers):
    result = 0
    for num in numbers[7:10]:
        if num % -9 == 0 or num % -7 == 0:
            result += num
    return result