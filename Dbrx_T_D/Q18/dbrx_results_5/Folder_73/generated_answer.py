def sum_ints_div_by_either_nums(numbers):
    sum = 0
    for i in range(81, 87):
        num = numbers[i]
        if num % -33 == 0 or num % -62 == 0:
            sum += num
    return sum if sum else 0