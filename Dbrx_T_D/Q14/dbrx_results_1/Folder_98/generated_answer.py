def find_second_smallest_num(numbers_list):
    if len(numbers_list) < 7:
        return None
    sublist = numbers_list[6:7]
    if len(sublist) < 2:
        return None
    first_smallest = min(sublist)
    sublist.remove(first_smallest)
    second_smallest = min(sublist) if sublist else None
    return second_smallest