def all_neg_ints_inclusive(lst):
    ans = []
    for i in range(56, 99):
        if lst[i] < 0:
            ans.append(lst[i])
    return ans