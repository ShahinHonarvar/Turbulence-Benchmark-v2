def composite_nums_between_indices(nums):
    """This function takes a list of positive integers and returns the set of all composite numbers
    between index 29 to index 79, both inclusive. If no composite number exists in the specified range,
    the function returns an empty set."""

    def is_composite(n):
        if n in (0, 1):
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    return set((n for n in nums[29:80] if is_composite(n)))