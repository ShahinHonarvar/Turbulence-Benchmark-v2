def all_odd_ints_exclusive(nums):
    """Return list of odd ints from 68 to 99, exclusive."""
    return [num for num in nums[68:99] if num % 2 != 0]