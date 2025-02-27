def all_neg_ints_exclusive(num):
    neg_nums = [n for n in num if n < 0 and 3 < num.index(n) < 8]
    return neg_nums or []