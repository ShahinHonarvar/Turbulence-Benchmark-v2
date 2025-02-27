def sum_ints_div_by_either_nums(numbers):
    sum = 0
    for i in range(281, 695):
        num = numbers[i]
        if num % -722 == 0 or num % -731 == 0:
            sum += num
    return sum