def sum_ints_div_by_either_nums(numbers):
    total = 0
    for num in numbers[14:94]:
        if num % 71 == 0 or num % 81 == 0:
            total += num
    return total