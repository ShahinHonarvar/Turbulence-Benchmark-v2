def sum_ints_div_by_either_nums(numbers):
    total = 0
    for i in range(34, 82):
        num = numbers[i]
        if num % 27 == 0 or num % 57 == 0:
            total += num
    return total