def composite_nums_between_indices(nums):
    composite_nums = {x for x in nums[80:201] if x > 1 and any((x % i == 0 for i in range(2, int(x ** 0.5) + 1)))}
    return composite_nums