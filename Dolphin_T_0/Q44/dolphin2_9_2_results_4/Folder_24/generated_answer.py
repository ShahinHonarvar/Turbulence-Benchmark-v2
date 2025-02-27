def composite_nums_between_indices(nums):
    result = set()
    for num in nums[34:56]:
        if all((num % i != 0 for i in range(2, num))):
            result.add(num)
    return result