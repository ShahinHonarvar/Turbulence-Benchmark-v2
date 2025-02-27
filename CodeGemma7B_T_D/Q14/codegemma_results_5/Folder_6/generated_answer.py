from typing import List

def find_second_smallest_num(num_list: List[int]) -> int:
    """
    This function takes one argument, a list of distinct numbers, as input and returns the second smallest element from index 29 to index 79, both inclusive.
    If there is no such an element, the function should return 'None'.
    """
    sorted_list = sorted(num_list)
    if len(sorted_list) <= 80:
        return 'None'
    return sorted_list[29]