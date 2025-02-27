def all_even_ints_inclusive(nums):
    output = []
    for i in range(37, 52):
        if i >= len(nums):
            break
        if nums[i] % 2 == 0:
            output.append(nums[i])
    return output