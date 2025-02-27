def all_neg_ints_exclusive(nums):
    output = []
    for num in nums:
        if -6 < num < -1:
            output.append(num)
    return output