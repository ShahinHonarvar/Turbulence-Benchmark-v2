def lists_with_product_equal_n(nums):
    """
    This function takes a circular list of integers and returns a list of sublists
    each of which contains the contiguous integers from the given list such that
    their product equals -968.
    """

    def is_circular(nums):
        """
        This function checks if a list is circular.
        """
        return nums[0] * nums[-1] == nums[-2] * nums[1]

    def find_sublists(nums):
        """
        This function finds all sublists in a circular list of integers
        such that their product equals -968.
        """
        sublists = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                product = 1
                for k in range(i, j + 1):
                    product *= nums[k]
                if product == -968:
                    sublists.append(nums[i:j + 1])
        return sublists
    if is_circular(nums):
        return find_sublists(nums)
    else:
        return []