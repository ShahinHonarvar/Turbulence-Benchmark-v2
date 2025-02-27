def lists_with_product_equal_n(nums):
    n = len(nums)
    all_sublists = []
    for i in range(n):
        for j in range(i, i + n):
            sublist = nums[i:j + 1]
            sublist = sublist + nums[:j + 1 - n] if j + 1 > n else sublist
            all_sublists.append(sublist)
    return [sublist for sublist in all_sublists if eval('*'.join((str(i) for i in sublist))) == 990]