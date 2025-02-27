def find_n_th_smallest_num(nums):
    """Sorts the list of numbers in ascending order and returns the 6th smallest number."""
    nums.sort()
    return nums[5]