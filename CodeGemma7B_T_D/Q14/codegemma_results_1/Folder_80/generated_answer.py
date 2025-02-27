def find_second_smallest_num(num_list):
    """
        Finds the second smallest number in a list from index 30 to index 87, inclusive. If there is no such number,
        the function returns 'None'.

        Args:
            num_list: A list of distinct numbers.

        Returns:
            The second smallest number in the list from index 30 to index 87, inclusive, or 'None' if
            there is no such number.
        """
    num_list = num_list[30:88]
    num_list.sort()
    if len(num_list) >= 2:
        return num_list[1]
    else:
        return 'None'