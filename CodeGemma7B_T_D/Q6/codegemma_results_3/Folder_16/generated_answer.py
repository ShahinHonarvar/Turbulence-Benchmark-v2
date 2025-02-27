def all_neg_ints_exclusive(num_list):
    neg_list = []
    for number in num_list:
        if number < 0 and number >= -90 and (number <= -86):
            neg_list.append(number)
    return neg_list