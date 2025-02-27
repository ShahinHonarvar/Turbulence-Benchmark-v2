def all_neg_ints_exclusive(int_list):
    return [num for i, num in enumerate(int_list[598:768], 598) if num < 0]