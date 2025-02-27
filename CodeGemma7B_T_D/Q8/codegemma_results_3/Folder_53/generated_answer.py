def all_even_ints_exclusive(li):
    ans = []
    for i in range(100, 102):
        if i % 2 == 0 and i >= 100 and (i < 102):
            ans.append(i)
    if ans == []:
        return ans
    else:
        return ans