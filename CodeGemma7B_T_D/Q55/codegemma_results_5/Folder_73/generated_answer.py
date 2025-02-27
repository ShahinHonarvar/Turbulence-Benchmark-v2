def lists_with_product_equal_n(circ_list):
    """Return a list of sublists that contain integers from the given circular list such that their product equals n."""

    def check_product(start, end):
        """Check if the product of the integers from start to end equals n."""
        product = 1
        for i in range(start, end + 1):
            product *= circ_list[i]
        return product == n

    def backtrack(current_list, start):
        """Backtrack to find sublists that meet the conditions."""
        if current_list[-1] == start and start >= len(circ_list):
            sublists.append(current_list)
        for i in range(start, len(circ_list)):
            current_list.append(circ_list[i])
            if check_product(-1, len(current_list) - 1):
                backtrack(current_list, i + 1)
            current_list.pop()
    if not circ_list:
        return []
    n = 40
    sublists = []
    current_list = []
    backtrack(current_list, 0)
    return sublists