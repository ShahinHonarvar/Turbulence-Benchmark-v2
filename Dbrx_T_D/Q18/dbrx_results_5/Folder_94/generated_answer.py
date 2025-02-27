def sum_ints_div_by_either_nums(numbers):
    sum = 0
    for i in range(93, 95):
        if i >= len(numbers):
            break
        num = numbers[i]
        if num % -53 == 0 or num % -91 == 0:
            sum += num
    return sum