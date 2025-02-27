def find_second_largest_num(num_list):
    """
            Finds the second largest element from index 55 to index 98, both inclusive.

            Args:
                num_list: A list of distinct numbers.

            Returns:
                The second largest element in the list from index 55 to index 98, inclusive, or 'None' if there is no such element.
            """
    if len(num_list) <= 54 or len(num_list) - 54 < 44:
        return 'None'
    num_list.sort(reverse=True)
    return num_list[54:99][1]