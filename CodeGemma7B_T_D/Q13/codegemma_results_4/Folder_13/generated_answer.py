def find_second_largest_num(lst):
    """
            Function finds the second largest element from index 25 to index 87 in a list of distinct numbers.

            Args:
                lst: A list of distinct numbers.

            Returns:
                The second largest element from index 25 to index 87 inclusive. If no such element exists, the function returns 'None'.
            """
    lst.sort(reverse=True)
    lst = lst[25:88]
    if len(lst) < 2:
        return 'None'
    return lst[1]