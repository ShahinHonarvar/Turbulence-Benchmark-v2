def composite_nums_between_indices(nums):
    comp_nums = set()
    for i in range(62, 100):
        if i < len(nums):
            num = nums[i]
            for j in range(2, num):
                if num % j == 0:
                    comp_nums.add(num)
                    break
    return comp_nums