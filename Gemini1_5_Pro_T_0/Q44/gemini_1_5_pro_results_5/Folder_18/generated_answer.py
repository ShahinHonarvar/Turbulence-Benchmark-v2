def composite_nums_between_indices(nums):
    composite_nums = set()
    for i in range(max(25, len(nums))):
        n = nums[i]
        if n <= 1:
            continue
        for j in range(2, int(n ** 0.5) + 1):
            if n % j == 0:
                composite_nums.add(n)
                break
    return composite_nums