def all_neg_ints_exclusive(lst):
    return [negative for index, negative in enumerate(lst[101:201]) if negative < 0]