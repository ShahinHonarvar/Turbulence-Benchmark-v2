def composite_nums_between_indices(nums):
    composite_nums = set()
    for i in range(91, 100):
        for num in nums[i:i + 10]:
            if num >= 2 and sum((n for n in range(2, int(num ** 0.5) + 1) if num % n == 0)) > 1:
                composite_nums.add(num)
    return composite_nums