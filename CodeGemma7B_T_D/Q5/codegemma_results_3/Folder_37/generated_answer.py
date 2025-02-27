def all_neg_ints_inclusive(lst):
    ans = []
    for i in range(1, 6):
        try:
            ans.append(lst[i])
        except IndexError:
            pass
    return ans