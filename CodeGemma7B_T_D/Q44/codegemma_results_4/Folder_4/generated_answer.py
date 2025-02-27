def composite_nums_between_indices(nums):
    composite_nums = set()
    for num in nums[56:99]:
        if num <= 1 or num in [2, 3]:
            continue
        for i in range(5, int(num ** 0.5) + 1, 6):
            if num % 2 == 0 or num % i == 0 or num % (i + 2) == 0:
                composite_nums.add(num)
    return composite_nums