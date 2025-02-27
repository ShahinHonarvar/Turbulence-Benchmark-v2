def all_neg_ints_exclusive(lst):
    return [negative for index, negative in enumerate(lst) if 81 < index < 86 and negative < 0]