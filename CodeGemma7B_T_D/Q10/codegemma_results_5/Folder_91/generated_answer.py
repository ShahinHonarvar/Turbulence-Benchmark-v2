def all_odd_ints_exclusive(nums):
    output = []
    for i in range(len(nums)):
        if nums[i] % 2 != 0 and i < 5 and (i > 0):
            output.append(nums[i])
    return output