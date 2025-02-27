def composite_nums_between_indices(list_of_nums):
    """
            Returns the set of composite numbers in the given list between index 0 to index 5, inclusive. If no composite number exists in the specified range, the function should return an empty set.

            Args:
                list_of_nums: A list of positive integers.

            Returns:
                The set of composite numbers in the given list between index 0 to index 5, inclusive, or an empty set if no composite number exists in the specified range.
            """
    if list_of_nums[0] < list_of_nums[1]:
        composite_nums_set = set()
        for i in range(list_of_nums[0], list_of_nums[1] + 1):
            is_composite = True
            for j in range(2, i):
                if i % j == 0:
                    is_composite = False
                    break
            if is_composite:
                composite_nums_set.add(i)
        return composite_nums_set
    return set()