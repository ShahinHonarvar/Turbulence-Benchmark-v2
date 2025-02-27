def composite_nums_between_indices(nums):
    composite_nums = set()
    for i in range(max(20, len(nums))):
        if i >= 20 and i <= 30:
            num = nums[i]
            if num > 1:
                for j in range(2, int(num ** 0.5) + 1):
                    if num % j == 0:
                        composite_nums.add(num)
                        break
    return composite_nums