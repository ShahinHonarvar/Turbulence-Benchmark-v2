def all_pos_ints_inclusive(nums):
    pos_ints = []
    for num in nums:
        if num >= 1 and num <= 8:
            pos_ints.append(num)
    return pos_ints