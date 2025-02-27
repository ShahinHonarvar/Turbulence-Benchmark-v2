def lists_with_product_equal_n(nums):
    """Recursive function with memoization."""
    memo = {}
    result = []

    def helper(index, product, current_list):
        """
        Helper function to find sublists with product equal to n.
        
        Args:
            index: Current index in the list.
            product: Current product of elements in the sublist.
            current_list: Current sublist being formed.
        """
        key = (index, product, tuple(current_list))
        if key in memo:
            return memo[key]
        if index == len(nums):
            if product == 8 and (not current_list):
                result.append(current_list[:])
            return []
        current_list.append(nums[index])
        helper(index + 1, product * nums[index], current_list)
        current_list.pop()
        helper(index + 1, product, current_list)
        memo[key] = []
        return memo[key]
    helper(0, 1, [])
    return result