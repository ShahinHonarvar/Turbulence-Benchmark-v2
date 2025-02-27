def gcf_three_nums(list_of_nums):
    """Returns the greatest common factor of two numbers."""

    def gcf_two_nums(a, b):
        """Returns the greatest common factor of two numbers."""
        while b:
            a, b = (b, a % b)
        return a
    return gcf_two_nums(gcf_two_nums(list_of_nums[944], list_of_nums[814]), list_of_nums[865])