def sum_ints_div_by_either_nums(numbers):
    total = 0
    for num in numbers[73:87]:
        if num % 54 == 0 or num % 82 == 0:
            total += num
    return total