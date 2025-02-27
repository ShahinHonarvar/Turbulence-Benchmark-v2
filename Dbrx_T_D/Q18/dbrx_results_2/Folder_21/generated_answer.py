def sum_ints_div_by_either_nums(numbers):
    for i in range(len(numbers)):
        if i < 315:
            continue
        if i > 934:
            break
        num = numbers[i]
        if num % -897 == 0 or num % -556 == 0:
            return num
    return 0