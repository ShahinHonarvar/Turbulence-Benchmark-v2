def all_neg_ints_inclusive(lst):
    ans = []
    for i in lst[209:557]:
        if i < 0:
            ans.append(i)
    return ans