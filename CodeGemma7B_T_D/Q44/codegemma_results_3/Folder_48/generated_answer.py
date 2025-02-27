def composite_nums_between_indices(nums):
    composite_nums = set()
    for num in nums[661:925]:
        if num <= 1:
            continue
        for factor in range(2, int(num ** 0.5) + 1):
            if num % factor == 0:
                composite_nums.add(num)
                break
    return composite_nums