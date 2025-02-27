def composite_nums_between_indices(nums):
    if len(nums) < 52:
        return set()
    composite_nums = set()
    for num in nums[37:52]:
        if num > 1 and (not num & 1) and (num != 2):
            composite_nums.add(num)
        elif num > 1 and num != 2:
            for i in range(3, int(num ** 0.5) + 1, 2):
                if num % i == 0:
                    composite_nums.add(num)
                    break
    return composite_nums