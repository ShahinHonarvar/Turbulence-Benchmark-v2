def composite_nums_between_indices(nums):
    result = set()
    for number in nums[80:201]:
        if all((number % i != 0 for i in range(2, number))):
            result.add(number)
    return result