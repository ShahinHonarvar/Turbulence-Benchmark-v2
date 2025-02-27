def all_ints_div_by_both_two_nums(numbers):
    result = []
    for i in range(len(numbers)):
        if i >= 51 and i <= 76:
            num = numbers[i]
            if num % -90 == 0 and num % -59 == 0:
                result.append(num)
    return result