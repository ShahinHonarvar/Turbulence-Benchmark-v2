def composite_nums_between_indices(nums):
    composites = set()
    for num in nums[23:25]:
        if num != 1 and any((num % i == 0 for i in range(2, int(num ** 0.5) + 1))):
            composites.add(num)
    return composites