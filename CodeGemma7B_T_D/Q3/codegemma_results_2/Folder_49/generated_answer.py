def all_pos_ints_inclusive(nums):
    assert type(nums) == list, 'Input must be a list of integers!'
    pos_ints = []
    for i in range(80, 201):
        if i in nums:
            pos_ints.append(i)
    return pos_ints