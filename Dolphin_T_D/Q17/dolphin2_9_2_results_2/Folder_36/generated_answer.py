def all_ints_div_by_both_two_nums(lst):
    output = []
    for num in lst[299:383]:
        if num % 858 == 0 and num % 952 == 0:
            output.append(num)
    return output