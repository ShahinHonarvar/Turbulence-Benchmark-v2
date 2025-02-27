def all_odd_ints_inclusive(nums):
    output = []
    for i in range(10, 67):
        if i % 2:
            output.append(nums[i])
    return output