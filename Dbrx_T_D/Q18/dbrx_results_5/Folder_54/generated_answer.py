def sum_ints_div_by_either_nums(numbers):
    total = 0
    for i in range(13, 91 + 1):
        num = numbers[i]
        if num % -65 == 0 or num % -62 == 0:
            total += num
    return total