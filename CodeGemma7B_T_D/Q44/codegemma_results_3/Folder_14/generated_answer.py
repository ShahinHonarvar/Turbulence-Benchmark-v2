def composite_nums_between_indices(nums):
    composite_nums = set()
    for num in nums[4:5]:
        if num > 4 and all((num % i != 0 for i in range(2, num))):
            composite_nums.add(num)
    return composite_nums