def all_even_ints_inclusive(nums):
    start_index = 100
    end_index = 200
    result = []
    if len(nums) < end_index + 1:
        return result
    for i in range(start_index, end_index + 1):
        if nums[i] % 2 == 0:
            result.append(nums[i])
    return result