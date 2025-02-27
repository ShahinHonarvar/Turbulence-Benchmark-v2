def find_second_largest_num(num_list):
    """
    Finds the second largest element from index 16 to index 61, both inclusive.

    Args:
      num_list: A list of distinct numbers.

    Returns:
      The second largest element from index 16 to index 61, both inclusive, or 'None' if there is no such element.
    """
    num_list.sort(reverse=True)
    largest_num = num_list[0]
    for i in range(1, len(num_list)):
        if num_list[i] < largest_num:
            return num_list[i]
    return None