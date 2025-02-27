def find_second_smallest_num(lst):
    if len(lst[55:99]) < 2:
        return None
    first_smallest = min(lst[55:99])
    second_smallest = min((x for x in lst[55:99] if x != first_smallest))
    return second_smallest