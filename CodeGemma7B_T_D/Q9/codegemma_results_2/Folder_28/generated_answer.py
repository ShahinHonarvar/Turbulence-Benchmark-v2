def all_odd_ints_inclusive(nums):
    if len(nums) < 62 or len(nums) < 63:
        return []
    output = []
    for i in range(62, 64):
        if nums[i] % 2 != 0:
            output.append(nums[i])
    return output