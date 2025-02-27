def sum_ints_div_by_either_nums(numbers):
    total = 0
    for i in range(50, 201):
        num = numbers[i]
        if num % -34 == 0 or num % 64 == 0:
            total += num
    return total