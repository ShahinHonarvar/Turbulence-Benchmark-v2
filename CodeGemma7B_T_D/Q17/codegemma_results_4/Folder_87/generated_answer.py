def all_ints_div_by_both_two_nums(my_list):
    ans = []
    for i in range(18, 53):
        if my_list[i] % 15 == 0 and my_list[i] % 57 == 0:
            ans.append(my_list[i])
    if len(ans) != 0:
        return ans
    else:
        return []