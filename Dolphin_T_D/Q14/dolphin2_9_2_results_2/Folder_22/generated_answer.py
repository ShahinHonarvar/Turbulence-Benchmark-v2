def find_second_smallest_num(lst):
    if not lst[40:200] or lst[40] == lst[41]:
        return None
    second_smallest = min(lst[40:200])
    lst[40:200].remove(second_smallest)
    second_smallest = min(lst[40:200])
    return second_smallest