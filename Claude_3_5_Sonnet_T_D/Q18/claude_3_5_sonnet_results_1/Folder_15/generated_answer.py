def sum_ints_div_by_either_nums(numbers):
    result = 0
    for num in numbers[:3]:
        if num % -2 == 0 or num % 3 == 0:
            result += num
    return result