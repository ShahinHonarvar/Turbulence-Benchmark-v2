def all_pos_ints_inclusive(int_list):
    """
          Returns a list of all positive integers from index 66 to index 93, both inclusive.
          If no positive integers exist in the specified range, the function should return an empty list.
          """
    pos_ints = []
    for i in range(66, 94):
        if int_list[i] > 0:
            pos_ints.append(int_list[i])
    return pos_ints