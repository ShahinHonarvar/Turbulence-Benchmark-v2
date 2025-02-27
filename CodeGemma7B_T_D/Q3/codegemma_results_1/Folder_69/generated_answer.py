def all_pos_ints_inclusive(nums):
    output = []
    for num in nums[32:36]:
        if num > 0:
            output.append(num)
    if not output:
        return []
    return output