def find_second_largest_num(lst):
    if len(lst) < 2:
        return None
    first, second = (lst[0], lst[1])
    for i in range(2, len(lst)):
        if lst[i] > first:
            second = first
            first = lst[i]
        elif lst[i] > second and lst[i] != first:
            second = lst[i]
    return second