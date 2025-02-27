def composite_nums_between_indices(nums):
    result_set = set()
    for num in nums[686:988]:
        if all((num % i != 0 for i in range(2, num))):
            result_set.add(num)
    return result_set