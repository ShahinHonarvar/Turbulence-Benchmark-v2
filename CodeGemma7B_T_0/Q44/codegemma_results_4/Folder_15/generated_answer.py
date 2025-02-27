def composite_nums_between_indices(nums):
    composite_set = set()
    for i in range(len(nums)):
        if i in range(0, 4):
            if nums[i] > 1 and (nums[i] % 2 == 0 or any((num % i == 0 for num in range(2, int(nums[i] ** 0.5) + 1)))):
                composite_set.add(nums[i])
    return composite_set