def find_second_largest_num(num_list):
    """Returns the second largest element from index 66 to index 93, both inclusive."""
    try:
        num_list_slice = sorted(num_list[66:94])[::-1][1]
        return num_list_slice
    except IndexError:
        return 'None'