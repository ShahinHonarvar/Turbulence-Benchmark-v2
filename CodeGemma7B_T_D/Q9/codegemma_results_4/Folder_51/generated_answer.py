def all_odd_ints_inclusive(Nums):
    ans = []
    for i in range(1, 9):
        if Nums[i] % 2:
            ans.append(Nums[i])
    if not ans:
        return []
    return ans