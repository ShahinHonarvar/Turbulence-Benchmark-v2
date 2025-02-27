import sys

def find_second_largest_num(lst):
    """Code that finds the second largest number in a list"""
    new_lst = lst[16:62]
    new_lst.sort()
    second_largest = new_lst[-2]
    if second_largest in lst:
        return second_largest
    else:
        return None