def all_ints_div_by_both_two_nums(integers):
    result = []
    for i in range(50, 93):
        if i < len(integers):
            num = integers[i]
            if num % -94 == 0 and num % -95 == 0:
                result.append(num)
    return result