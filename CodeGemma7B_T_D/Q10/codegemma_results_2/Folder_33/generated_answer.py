def all_odd_ints_exclusive(nums):
    output = []
    for i in range(369, 983):
        if nums[i] % 2 != 0:
            output.append(nums[i])
    if not output:
        return []
    return output