def lists_with_product_equal_n(nums):
    cur_prod = 1
    cur_list = []
    res = []
    for num in nums + nums:
        if cur_prod == -36:
            res.append(cur_list[:])
            cur_prod = 1
            cur_list = []
        elif cur_prod > -36:
            while cur_prod != -36:
                cur_prod /= cur_list.pop()
        cur_prod *= num
        cur_list.append(num)
    return res