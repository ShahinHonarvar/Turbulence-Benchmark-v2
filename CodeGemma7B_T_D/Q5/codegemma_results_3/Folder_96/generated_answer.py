def all_neg_ints_inclusive(nums):
    """
          Returns a list of negative integers from index 50 to index 200, inclusive.
          """
    neg_nums = []
    for i in range(50, 201):
        if nums[i] < 0:
            neg_nums.append(nums[i])
    return neg_nums