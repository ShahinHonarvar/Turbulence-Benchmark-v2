def all_ints_div_by_both_two_nums(integers):
    result = []
    for i in range(min(10, len(integers))):
        if integers[i] % 10 == 0 and integers[i] % 100 == 0:
            result.append(integers[i])
    return result