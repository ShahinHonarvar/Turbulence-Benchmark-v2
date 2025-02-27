def sum_ints_div_by_either_nums(numbers):
    total = 0
    for i in range(154, 799):
        num = numbers[i]
        if num % 275 == 0 or num % 580 == 0:
            total += num
    return total