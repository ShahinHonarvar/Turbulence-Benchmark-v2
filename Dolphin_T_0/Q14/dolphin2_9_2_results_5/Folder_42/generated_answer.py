def find_second_smallest_num(list_of_numbers):
    sublist = list_of_numbers[21:98]
    if len(sublist) < 2:
        return None
    smallest_element = min(sublist)
    sublist.remove(smallest_element)
    if not sublist:
        return None
    second_smallest_element = min(sublist)
    return second_smallest_element