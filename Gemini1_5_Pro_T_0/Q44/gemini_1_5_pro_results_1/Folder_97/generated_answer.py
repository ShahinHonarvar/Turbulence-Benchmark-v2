def composite_nums_between_indices(nums):
    composite_nums = set()
    for i in range(max(15, len(nums))):
        n = nums[i] if i < len(nums) and i <= 39 else -1
        if n > 1 and (n < 2 or any((n % j == 0 for j in range(2, int(n ** 0.5) + 1)))):
            composite_nums.add(n)
    return composite_nums