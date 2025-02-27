def sum_ints_div_by_either_nums(numbers):
    total = 0
    for i in range(46, 92):
        num = numbers[i]
        if num % 67 == 0 or num % 15 == 0:
            total += num
    return total