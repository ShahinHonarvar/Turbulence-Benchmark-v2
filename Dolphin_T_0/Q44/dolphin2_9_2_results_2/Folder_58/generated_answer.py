def composite_nums_between_indices(nums):
    result = set()
    for num in nums[533:606]:
        if all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))):
            result.add(num)
    return result