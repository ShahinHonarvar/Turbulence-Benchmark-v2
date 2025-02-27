def all_ints_div_by_both_two_nums(l):
    ans = []
    for i in range(20, 36):
        if l[i] % -36 == 0 and l[i] % -89 == 0:
            ans.append(l[i])
    if len(ans) == 0:
        return []
    else:
        return ans