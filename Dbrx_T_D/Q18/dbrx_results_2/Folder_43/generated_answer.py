def sum_ints_div_by_either_nums(numbers):
    sum = 0
    for i in range(57, 86):
        if i < 0 or i >= len(numbers):
            continue
        num = numbers[i]
        if num % -77 == 0 or num % -32 == 0:
            sum += num
    return sum