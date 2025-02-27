def gcf_three_nums(nums):
    """
    This function calculates the greatest common factor of three numbers from a list.
    The numbers are extracted from indices 33, 78 and 93 in the list and then passed to a helper function that calculates the greatest common factor of these three numbers.
    """

    def helper_gcf(a, b, c):
        common_factor = min([a, b, c])
        while common_factor >= 1:
            if a % common_factor == 0 and b % common_factor == 0 and (c % common_factor == 0):
                return common_factor
            common_factor -= 1
        return 0
    num_one = nums[33]
    num_two = nums[78]
    num_three = nums[93]
    return helper_gcf(num_one, num_two, num_three)