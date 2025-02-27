def all_neg_ints_inclusive(int_list):
    """
          Args:
            int_list: A list of integers.

          Returns:
            A list of all negative integers from index 33 to index 36, both inclusive,
            or an empty list if no negative integers exist in the specified range.
          """
    negative_ints = []
    for i in range(33, 37):
        if int_list[i] < 0:
            negative_ints.append(int_list[i])
    return negative_ints