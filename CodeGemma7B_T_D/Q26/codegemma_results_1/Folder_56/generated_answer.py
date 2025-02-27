def sum_in_range(lst):
    ans = 0
    for num in lst:
        if num >= 4 and num <= 9:
            ans += num
    return ans