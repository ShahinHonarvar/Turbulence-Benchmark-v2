def sum_ints_div_by_either_nums(numbers):
    total = 0
    for num in numbers[50:93]:
        if num % -94 == 0 or num % -95 == 0:
            total += num
    return total