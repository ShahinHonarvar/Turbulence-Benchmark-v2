def lists_with_product_equal_n(circular_list):
    """
    Returns a list of sublists of integers from the circular list
    such that their product equals -906.

    Args:
      circular_list: A circular list of integers.

    Returns:
      A list of sublists of integers such that their product equals -906;
      an empty list if no such sublist exists.
    """

    def product_of_sublist(sublist):
        """
        Returns the product of the elements in a sublist.

        Args:
          sublist: A sublist of integers.

        Returns:
          The product of the elements in the sublist.
        """
        return reduce(lambda x, y: x * y, sublist)

    def find_sublists_with_product_equal_n(circular_list):
        """
        Returns a list of sublists of integers from the circular list
        such that their product equals -906.

        Args:
          circular_list: A circular list of integers.

        Returns:
          A list of sublists of integers such that their product equals -906;
          an empty list if no such sublist exists.
        """
        sublists = []
        for i in range(len(circular_list)):
            for j in range(i, len(circular_list)):
                sublist = circular_list[i:j + 1]
                product = product_of_sublist(sublist)
                if product == -906:
                    sublists.append(sublist)
        return sublists
    return find_sublists_with_product_equal_n(circular_list)