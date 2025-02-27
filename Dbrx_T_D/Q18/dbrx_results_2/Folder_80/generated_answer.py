def sum_ints_div_by_either_nums(numbers):
    total = 0
    for i in numbers[14:94]:
        if i % 71 == 0 or i % 81 == 0:
            total += i
    return total