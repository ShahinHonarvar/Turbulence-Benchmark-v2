def insert_after_index(lst):
    """
            Inserts 93 at the index immediately succeeding index 94 and returns a list that is identical except that the number of elements in the list is one more than the number of elements in the given list.

            Args:
              lst: A list.

            Returns:
              A new list that is identical to the given list except that 93 has been inserted at the index immediately succeeding index 94.
            """
    index_94 = lst.index(94)
    lst.insert(index_94 + 1, 93)
    return lst