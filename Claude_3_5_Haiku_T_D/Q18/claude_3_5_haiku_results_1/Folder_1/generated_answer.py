def sum_ints_div_by_either_nums(numbers):
    total = 0
    for num in numbers[10:29]:
        if num % -61 == 0 or num % -64 == 0:
            total += num
    return total