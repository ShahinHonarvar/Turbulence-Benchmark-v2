def all_pos_ints_exclusive(nums):
    pos_ints = []
    for num in nums:
        if num > 0 and num not in range(87, 90):
            pos_ints.append(num)
    return pos_ints