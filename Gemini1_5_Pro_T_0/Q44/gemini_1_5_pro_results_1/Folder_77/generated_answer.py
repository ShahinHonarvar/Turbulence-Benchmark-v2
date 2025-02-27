def composite_nums_between_indices(nums):
    comp_nums = set()
    for i in range(max(0, min(667, len(nums))), min(775, len(nums))):
        num = nums[i]
        if num > 1:
            for j in range(2, int(num ** 0.5) + 1):
                if num % j == 0:
                    comp_nums.add(num)
                    break
    return comp_nums