def lists_with_product_equal_n(nums, n=-95):
    len_nums = len(nums)
    cycles = []
    for i in range(len_nums):
        new_list = nums[i:len_nums] + nums[0:i]
        cycles.append(new_list)
    sublists = {}
    for cycle_nums in cycles:
        for i in range(len(cycle_nums)):
            for j in range(i + 1, len(cycle_nums) + 1):
                prod = 1
                for k in range(i, j):
                    prod *= cycle_nums[k]
                if prod == n:
                    sublist = cycle_nums[i:j]
                    if sublist not in sublists.values():
                        sublists[len(sublist)] = sublist
    return list(sublists.values())