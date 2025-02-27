def all_neg_ints_inclusive(nums):
    output = []
    for i in range(10, 101):
        if nums[i] < 0:
            output.append(nums[i])
    return output.copy()