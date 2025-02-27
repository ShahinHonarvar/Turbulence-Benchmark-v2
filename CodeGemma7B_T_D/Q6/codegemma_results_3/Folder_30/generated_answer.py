def all_neg_ints_exclusive(ls):
    ans = [num for num in ls[86:89] if num < 0]
    if not ans:
        ans = []
    return ans