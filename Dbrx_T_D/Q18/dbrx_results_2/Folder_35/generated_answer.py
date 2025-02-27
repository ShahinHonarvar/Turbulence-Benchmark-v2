def sum_ints_div_by_either_nums(numbers):
    sum = 0
    for i in range(77, 88):
        num = numbers[i]
        if num % 23 == 0 or num % 57 == 0:
            sum += num
    return sum