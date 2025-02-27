def find_n_th_smallest_num(nums):
    """
    This function takes a list of distinct numbers as input and returns the 17th smallest number from index 0 to index 16, both inclusive.
    """
    nums.sort()
    return nums[16]