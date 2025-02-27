def composite_nums_between_indices(nums):
    result = set()
    for i in range(246, 751):
        num = nums[i]
        if num > 1 and (not all((num % j for j in range(2, num)))):
            result.add(num)
    return result