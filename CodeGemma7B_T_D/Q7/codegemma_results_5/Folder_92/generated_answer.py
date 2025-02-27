def all_even_ints_inclusive(nums):
    out = []
    for i in range(len(nums)):
        if i >= 0 and i <= 1 and (nums[i] % 2 == 0):
            out.append(nums[i])
    return out