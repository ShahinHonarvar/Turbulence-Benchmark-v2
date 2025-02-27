def all_neg_ints_exclusive(lst):
    ans = []
    for i, e in enumerate(lst):
        if -55 <= i <= -35 and e < 0:
            ans.append(e)
    return ans