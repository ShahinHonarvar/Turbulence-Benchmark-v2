def sum_ints_div_by_either_nums(numbers):
    total = 0
    for i in range(3):
        num = numbers[i]
        if num % -2 == 0 or num % 3 == 0:
            total += num
    return total