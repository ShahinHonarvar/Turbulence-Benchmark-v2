def sum_ints_div_by_either_nums(numbers):
    for i in range(32, 100):
        num = numbers[i]
        if num % -11 == 0 or num % -15 == 0:
            if i + 1 < len(numbers):
                return num + sum_ints_div_by_either_nums(numbers[i + 1:])
    return 0