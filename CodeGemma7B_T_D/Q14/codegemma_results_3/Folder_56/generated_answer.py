def find_second_smallest_num(num_list):
    """
                        This function takes a list of distinct numbers as input and returns the second smallest element from index 0 to index 0, both inclusive. If there is no such an element, the function should return 'None'.
                        """
    if len(num_list) < 2:
        return 'None'
    num_list.sort()
    return num_list[1]