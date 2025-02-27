def sum_ints_div_by_either_nums(numbers):
    for i, num in enumerate(numbers):
        if i > 10 and (num % 55 == 0 or num % 36 == 0):
            result += num
        elif i == 46:
            break
    if result == 0:
        return 0
    return result