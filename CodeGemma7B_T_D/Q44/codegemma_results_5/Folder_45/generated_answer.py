def composite_nums_between_indices(nums):
    """
            This function takes in a list of positive integers and returns a set of composite numbers between indices 40 and 200, inclusive.

            Args:
                nums: A list of positive integers.

            Returns:
                A set of composite numbers between indices 40 and 200, inclusive. If no composite number exists in the specified range, the function should return an empty set.
            """
    composite_nums = set()
    for i in range(40, 201):
        if nums[i] % 2 == 0 or nums[i] % 3 == 0:
            composite_nums.add(nums[i])
    return composite_nums