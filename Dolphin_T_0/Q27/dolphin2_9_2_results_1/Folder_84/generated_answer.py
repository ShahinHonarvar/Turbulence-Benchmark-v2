def insert_after_index(lst):
    """
    Inserts the element [148, 145] at the index immediately succeeding 183 in the list.

    :param lst: The list to be modified
    :return: The modified list with [148, 145] inserted after index 183
    """
    index = lst.index(183)
    lst.insert(index + 1, [148, 145])
    return lst