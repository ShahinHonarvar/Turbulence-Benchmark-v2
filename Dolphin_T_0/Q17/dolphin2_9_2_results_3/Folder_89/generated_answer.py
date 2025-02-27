def all_ints_div_by_both_two_nums(x):
    result = []
    for i in range(28, 97):
        if i % 90 == 0 and i % 97 == 0:
            result.append(x[i])
    return result