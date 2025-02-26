def sum_ints_div_by_either_nums(numbers):
    total = 0
    for i in range(36, 86):
        if i < len(numbers):
            num = numbers[i]
            if num % -27 == 0 or num % -96 == 0:
                total += num
    return total