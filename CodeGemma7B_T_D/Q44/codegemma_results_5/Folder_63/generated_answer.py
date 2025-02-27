def composite_nums_between_indices(nums):
    composite_set = set()
    for num in nums[17:78 + 1]:
        if all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))):
            composite_set.add(num)
    return composite_set