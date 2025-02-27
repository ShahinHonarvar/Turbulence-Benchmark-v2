def find_second_largest_num(lst):
    """
    This function takes a list of distinct numbers as input and returns the second largest element from index 10 to index 66, both inclusive. If there is no such element, the function should return 'None'.
    """
    sublst = lst[10:67]
    sublst.sort(reverse=True)
    if len(sublst) < 2:
        return None
    else:
        return sublst[1]