def all_neg_ints_exclusive(nums):
    output = []
    for i in range(389, 748):
        if nums[i] < 0:
            output.append(nums[i])
    return output