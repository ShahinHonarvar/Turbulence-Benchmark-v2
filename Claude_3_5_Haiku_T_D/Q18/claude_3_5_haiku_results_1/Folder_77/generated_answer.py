def sum_ints_div_by_either_nums(numbers):
    total = 0
    for num in numbers[828:933]:
        if num % -649 == 0 or num % -461 == 0:
            total += num
    return total