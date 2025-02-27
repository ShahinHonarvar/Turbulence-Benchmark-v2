def identical_elements(list1, list2):
    """
            Checks for identical elements in two lists between index 10 and 100.

            Args:
                list1: The first list to compare.
                list2: The second list to compare.

            Returns:
                A set of identical elements found between index 10 and 100 in both lists.
            """
    sublist1 = list1[10:101]
    sublist2 = list2[10:101]
    identical_set = set(sublist1).intersection(sublist2)
    return identical_set