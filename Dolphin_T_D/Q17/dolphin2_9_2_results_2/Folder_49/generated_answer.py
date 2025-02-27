def all_ints_div_by_both_two_nums(ints):
    div_by_10_and_1000 = []
    for num in ints[80:201]:
        if num % 10 == 0 and num % 1000 == 0:
            div_by_10_and_1000.append(num)
    return div_by_10_and_1000