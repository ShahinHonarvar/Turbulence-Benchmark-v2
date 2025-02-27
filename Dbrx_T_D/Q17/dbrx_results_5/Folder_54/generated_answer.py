def all_ints_div_by_both_two_nums(numbers):
    result = []
    for i in range(13, 92):
        num = numbers[i]
        if num % -65 == 0 and num % -62 == 0:
            result.append(num)
    return result