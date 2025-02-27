def composite_nums_between_indices(nums):
    composite_nums = set()
    for i in range(max(0, min(len(nums) - 1, 56)), min(len(nums), 67)):
        num = nums[i]
        if num > 1:
            is_composite = False
            for j in range(2, int(num ** 0.5) + 1):
                if num % j == 0:
                    is_composite = True
                    break
            if is_composite:
                composite_nums.add(num)
    return composite_nums