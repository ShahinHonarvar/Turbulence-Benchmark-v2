def all_odd_ints_inclusive(nums):
    output = []
    for i in range(43, 87):
        if i >= 43 and i <= 86 and (nums[i] % 2 == 1):
            output.append(nums[i])
    return output