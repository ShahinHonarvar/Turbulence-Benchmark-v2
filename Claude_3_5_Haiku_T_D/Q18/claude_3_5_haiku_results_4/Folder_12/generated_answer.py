def sum_ints_div_by_either_nums(numbers):
    total = 0
    for num in numbers[35:65]:
        if num % -30 == 0 or num % -95 == 0:
            total += num
    return total