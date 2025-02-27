def sum_ints_div_by_either_nums(numbers):
    for i in range(86, 90):
        if i >= len(numbers):
            continue
        num = numbers[i]
        if num % -61 == 0 or num % -79 == 0:
            return num
    return 0