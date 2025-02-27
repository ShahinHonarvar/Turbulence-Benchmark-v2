def lists_with_product_equal_n(circular_list):
    """
        Args:
                circular_list: A circular list of integers.

        Returns:
                A list of sublists each of which contains the contiguous integers from the given list such that their product equals -91.
        """

    def get_product(lst):
        product = 1
        for num in lst:
            product *= num
        return product
    result = []
    for i in range(len(circular_list)):
        for j in range(i + 1, len(circular_list) + 1):
            sublist = circular_list[i:j]
            if len(sublist) <= len(circular_list) and get_product(sublist) == -91:
                if not sublist in result:
                    result.append(sublist)
    return result