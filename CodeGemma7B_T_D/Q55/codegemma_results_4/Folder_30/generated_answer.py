def lists_with_product_equal_n(c_nums):
    i = 0
    j = 0
    ans = []
    while i < len(c_nums):
        curr_product = 1
        cur = i
        while j < len(c_nums):
            j = cur
            while j < len(c_nums):
                curr_product *= c_nums[j]
                j += 1
            if curr_product == 99:
                tt = c_nums[cur:j]
                if tt not in ans:
                    ans.append(tt)
            curr_product = 1
            cur += 1
        i += 1
    return ans