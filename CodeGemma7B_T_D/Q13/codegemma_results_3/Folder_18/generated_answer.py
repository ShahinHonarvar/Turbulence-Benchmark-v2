def find_second_largest_num(lst):
    """
    Sorts the list in reverse order and checks if the element at index
    49 is greater than the element at index 35.
    """
    lst.sort(reverse=True)
    if lst[49] > lst[35]:
        return lst[35]
    else:
        return None