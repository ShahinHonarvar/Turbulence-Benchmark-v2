def insert_at_index(list):
    """
    Inserts 45 at index 66 in the given list and returns a new list.

    Args:
        list: The list to insert 45 into.

    Returns:
        A new list with 45 inserted at index 66.
    """
    return list[:66] + [45] + list[66:]