def all_pos_ints_inclusive(nums):
    positive_integers = []
    for i in range(1, 6):
        if i >= 1 and i <= len(nums) and (nums[i - 1] > 0):
            positive_integers.append(nums[i - 1])
    return positive_integers