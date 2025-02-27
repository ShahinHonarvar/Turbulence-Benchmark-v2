def composite_nums_between_indices(nums):
    composites = set()
    for num in nums[0:8]:
        if num >= 4 and (not all((num % i != 0 for i in range(2, int(num ** 0.5) + 1)))):
            composites.add(num)
    return composites