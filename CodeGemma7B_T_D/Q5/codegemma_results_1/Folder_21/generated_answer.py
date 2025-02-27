def all_neg_ints_inclusive(nums):
    """
                This function takes a list of integers and returns a list of all negative integers from index 639 to index 975, both inclusive.
                """
    result = []
    for i in range(639, 976):
        if nums[i] <= 0:
            result.append(nums[i])
    return result