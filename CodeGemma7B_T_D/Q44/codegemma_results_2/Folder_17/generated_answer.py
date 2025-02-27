def composite_nums_between_indices(nums):
    composite_nums = set()
    for num in nums[50:55]:
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    composite_nums.add(num)
    return composite_nums