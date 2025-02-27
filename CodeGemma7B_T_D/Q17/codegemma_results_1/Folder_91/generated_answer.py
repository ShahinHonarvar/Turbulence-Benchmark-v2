def all_ints_div_by_both_two_nums(lst):
    ans = []
    for i in range(5):
        if lst[i] % 8 == 0 and lst[i] % -3 == 0:
            ans.append(lst[i])
    return ans