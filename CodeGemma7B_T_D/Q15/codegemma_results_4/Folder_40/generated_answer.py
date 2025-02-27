def sum_odd_ints_inclusive(nums):
    """
                Sums all odd integers in a list from index 0 to index 2, both inclusive.

                Args:
                nums: A list of integers.

                Returns:
                The sum of all odd integers from index 0 to index 2, both inclusive, or 0 if no odd integers exist in the range.
            """
    if not nums or len(nums) <= 2:
        return 0
    sum_odd = 0
    for i in range(3):
        if nums[i] % 2 != 0:
            sum_odd += nums[i]
    return sum_odd