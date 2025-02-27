def composite_nums_between_indices(nums):
    composites = set()
    for num in nums[62:64]:
        if num > 1 and all((num % i != 0 for i in range(2, num))):
            composites.add(num)
    return composites