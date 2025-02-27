def sum_ints_div_by_either_nums(numbers):
    total = 0
    for i in range(14, 94):
        num = numbers[i]
        if num % 71 == 0 or num % 81 == 0:
            total += num
    return total