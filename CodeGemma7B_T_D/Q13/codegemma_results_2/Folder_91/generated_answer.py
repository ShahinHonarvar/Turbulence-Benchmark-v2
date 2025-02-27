def find_second_largest_num(num_list):
    """
    This function takes a list of distinct numbers and returns the second largest
    element from index 0 to index 5, both inclusive. If there is no such
    element, the function returns 'None'.
    """
    try:
        num_list.sort(reverse=True)
        return num_list[1:6]
    except IndexError:
        return None