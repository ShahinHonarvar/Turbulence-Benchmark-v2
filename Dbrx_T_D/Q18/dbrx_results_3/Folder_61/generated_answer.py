def sum_ints_div_by_either_nums(numbers):
    total = 0
    for i in range(0, 7):
        if i >= len(numbers):
            break
        num = numbers[i]
        if num % -5 == 0 or num % -6 == 0:
            total += num
    return total