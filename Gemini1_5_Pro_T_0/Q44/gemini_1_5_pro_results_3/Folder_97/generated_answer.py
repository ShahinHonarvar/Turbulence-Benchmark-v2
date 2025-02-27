def composite_nums_between_indices(nums):
    composite_nums = set()
    for i in range(max(15, len(nums))):
        for j in range(min(40, len(nums)) + 1):
            n = nums[i]
            if n > 1:
                for i in range(2, int(n ** 0.5) + 1):
                    if n % i == 0:
                        composite_nums.add(n)
                        break
    return composite_nums