def find_second_smallest_num(lst):
    if 639 <= len(lst) <= 975:
        spliced = lst[638:976]
        if len(set(spliced)) < 2:
            return None
        else:
            smallest = min(spliced)
            second_smallest = min([i for i in spliced if i > smallest])
            return second_smallest
    else:
        return None