def find_second_smallest_num(num_list):
    """
            Returns the second smallest element from index 42 to index 68, both inclusive. If there is no such element,
            the function should return 'None'.
            """
    if not num_list or len(num_list) < 43 or num_list[41] >= num_list[42]:
        return None
    second_smallest = num_list[42]
    for i in range(43, 69):
        if num_list[i] < second_smallest:
            second_smallest = num_list[i]
    return second_smallest