def sum_ints_div_by_either_nums(numbers):
    sum = 0
    for i in range(200, 202):
        num = numbers[i]
        if num % 17 == 0 or num % -5 == 0:
            sum += num
    return sum