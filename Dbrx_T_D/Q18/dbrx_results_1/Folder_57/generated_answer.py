def sum_ints_div_by_either_nums(numbers):
    total = 0
    for i in range(51, 77):
        num = numbers[i]
        if num % -90 == 0 or num % -59 == 0:
            total += num
    return total