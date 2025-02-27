def composite_nums_between_indices(nums):
    composite_nums = set()
    for num in nums[1:9]:
        if all((num % i != 0 for i in range(2, num))):
            continue
        composite_nums.add(num)
    return composite_nums