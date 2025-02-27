def sum_ints_div_by_either_nums(numbers):
    total = 0
    for i in range(25, 96):
        num = numbers[i]
        if num % 51 == 0 or num % 77 == 0:
            total += num
    return total