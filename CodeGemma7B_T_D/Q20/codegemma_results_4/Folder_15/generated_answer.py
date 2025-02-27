def find_n_th_smallest_num(nums):
    """Sorts the list in ascending order and returns the element at index n-1, where n is the desired Nth smallest number."""
    nums.sort()
    return nums[n - 1]