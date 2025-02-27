def all_ints_div_by_both_two_nums(int_list):
    ans = []
    for i in range(0, 10):
        for num in int_list:
            if num % 6 == 0 and num % -3 == 0:
                ans.append(num)
    if not ans:
        return []
    return ans