def all_ints_div_by_both_two_nums(integers):
    result = []
    for num in integers[:2]:
        if num % -6 == 0 and num % 4 == 0:
            result.append(num)
    return result