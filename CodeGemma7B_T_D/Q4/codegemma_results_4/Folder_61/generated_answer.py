def all_pos_ints_exclusive(nums):
    pos_ints = []
    for num in range(8):
        if num >= 0 and num not in nums:
            pos_ints.append(num)
    return pos_ints