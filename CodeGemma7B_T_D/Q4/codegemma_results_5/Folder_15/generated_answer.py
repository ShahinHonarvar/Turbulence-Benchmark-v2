def all_pos_ints_exclusive(nums):
    positive_ints = []
    for num in nums:
        if num > 0 and num < 4:
            positive_ints.append(num)
    return positive_ints