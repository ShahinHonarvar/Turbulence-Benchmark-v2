from typing import CircularList, List

def lists_with_product_equal_n(circular_list: CircularList[int]) -> List[List[int]]:
    """Return a list of sublists each of which contains the contiguous integers from the given list such that their product equals -91."""
    result = []
    current_sublist = []
    current_product = 1
    for i in range(len(circular_list)):
        current_sublist.append(circular_list[i])
        current_product *= circular_list[i]
        while current_product > -91 and current_sublist:
            current_product //= current_sublist.pop(0)
        if current_product == -91:
            result.append(current_sublist[:])
    return result