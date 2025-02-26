def sum_ints_div_by_either_nums(numbers):
    total = 0
    for num in numbers[:9]:
        if num % -3 == 0 or num % 8 == 0:
            total += num
    return total