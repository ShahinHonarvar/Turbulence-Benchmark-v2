def sum_ints_div_by_either_nums(numbers):
    for i in range(len(numbers)):
        if i >= 13 and i <= 91:
            num = numbers[i]
            if num % -65 == 0 or num % -62 == 0:
                sum += num
    return sum