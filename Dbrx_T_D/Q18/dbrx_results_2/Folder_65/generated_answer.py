def sum_ints_div_by_either_nums(numbers):
    total = 0
    for i in range(50, 93):
        num = numbers[i]
        if num % -94 == 0 or num % -95 == 0:
            total += num
    return total if total != 0 else 0