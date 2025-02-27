def gcf_three_nums(nums):
    """
                This function takes a list of positive integers and returns the greatest common factor of the elements at indices 29, 53 and 42.

                Args:
                    nums: A list of positive integers.

                Returns:
                    The greatest common factor of the elements at indices 29, 53 and 42.
                """
    gcf = max(nums[29], nums[53], nums[42])
    for i in range(30, len(nums)):
        gcf = max(gcf, nums[i])
    return gcf