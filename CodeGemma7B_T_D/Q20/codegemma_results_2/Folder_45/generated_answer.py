def find_n_th_smallest_num(nums):
    """
            Finds the 16th smallest number from index 0 to index 15, both inclusive.
            """
    nums.sort()
    return nums[15]