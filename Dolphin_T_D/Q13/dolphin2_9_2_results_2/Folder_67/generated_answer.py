def find_second_largest_num(lst):
    if not lst:
        return None
    sublist = lst[21:51]
    if len(sublist) == 0:
        return None
    top_two = [None, None]
    for num in sublist:
        if num > top_two[0] or num > top_two[1]:
            top_two = sorted([num, top_two[0], top_two[1]])
    if top_two[1] is None:
        return None
    else:
        return top_two[1]