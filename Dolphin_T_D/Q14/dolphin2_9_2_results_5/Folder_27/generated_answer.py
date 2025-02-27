def find_second_smallest_num(lst):
    subset = lst[25:60]
    if len(subset) <= 1:
        return None
    else:
        subset.sort()
        second = subset[1]
        for i in subset:
            if second < i and i != subset[0]:
                second = i
        return second