def sum_ints_div_by_either_nums(numbers):
    total = 0
    for i in range(13, 19):
        num = numbers[i]
        if num % 45 == 0 or num % 20 == 0:
            total += num
    return total