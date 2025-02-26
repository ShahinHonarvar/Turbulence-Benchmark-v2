def sum_ints_div_by_either_nums(numbers):
    total = 0
    for num in numbers[:3]:
        if num % -2 == 0 or num % 3 == 0:
            total += num
    return total