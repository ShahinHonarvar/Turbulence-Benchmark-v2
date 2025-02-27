def all_pos_ints_inclusive(nums):
    output = []
    for i in range(262, 747):
        if i in nums:
            output.append(i)
    return output