def find_second_largest_num(lst):
    """
            Finds the second largest element from index 10 to index 66, inclusive.
            """
    lst.sort(reverse=True)
    if len(lst) < 2:
        return None
    if 10 <= len(lst) <= 66:
        return lst[9]
    else:
        return None