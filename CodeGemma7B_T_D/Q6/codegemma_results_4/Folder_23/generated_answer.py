def all_neg_ints_exclusive(num_list):
    new_list = []
    for num in num_list:
        if -29 < num < -53 and num not in new_list:
            new_list.append(num)
    return new_list