def all_ints_not_div_by_num(lst):
    ans = []
    for i in range(32, 44):
        if i not in lst or lst[i] % 34 != 0:
            ans.append(lst[i])
    return ans