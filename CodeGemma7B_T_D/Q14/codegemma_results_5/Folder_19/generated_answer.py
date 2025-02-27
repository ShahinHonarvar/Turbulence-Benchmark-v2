def find_second_smallest_num(lst):
    """
          This function takes one argument, a list of distinct numbers, as input and returns the second smallest element from index 4 to index 8, both inclusive. If there is no such an element, the function should return 'None'.
          """
    if len(lst) <= 8 or len(lst) < 5:
        return None
    second_smallest_num = lst[4]
    for i in range(5, 9):
        if lst[i] < second_smallest_num:
            second_smallest_num = lst[i]
    return second_smallest_num