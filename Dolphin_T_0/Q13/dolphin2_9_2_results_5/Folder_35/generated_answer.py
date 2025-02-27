def find_second_largest_num(lst):
    subset = lst[30:49]
    if len(subset) < 2:
        return None
    first = max(subset[0], subset[1])
    second = min(subset[0], subset[1])
    for num in subset[2:]:
        if num > first:
            second = first
            first = num
        elif num > second and num < first:
            second = num
    if second == first:
        return None
    return second