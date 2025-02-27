def all_pos_ints_exclusive(nums):
    output = []
    for num in nums[50:77]:
        if num > 0:
            output.append(num)
    if len(output) == 0:
        return []
    return output