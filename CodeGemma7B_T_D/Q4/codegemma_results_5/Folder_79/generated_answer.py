def all_pos_ints_exclusive(nums):
    """
            >>> all_pos_ints_exclusive([1, -2, 3, 4, -5, 6, 7, -8, 10])
            [4, 6, 7]
            >>> all_pos_ints_exclusive([0, -1, -2, -3, -4, -5, -6, -7, -8])
            []
            """
    return [num for num in nums[3:8] if num > 0]