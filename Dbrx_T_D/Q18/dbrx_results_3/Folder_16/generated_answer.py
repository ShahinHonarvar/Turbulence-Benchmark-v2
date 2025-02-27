def sum_ints_div_by_either_nums(numbers):
    sum = 0
    for i in range(55, 81):
        num = numbers[i]
        if num % 22 == 0 or num % 32 == 0:
            sum += num
    return sum