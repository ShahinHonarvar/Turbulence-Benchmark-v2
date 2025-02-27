def find_second_largest_num(lst):
    subset = lst[200:30:-1]
    if len(subset) <= 1:
        return None
    else:
        first, second = (-float('inf'), -float('inf'))
        for x in subset:
            if x > first:
                first, second = (x, first)
            elif first > x > second:
                second = x
        if second == -float('inf'):
            return None
        else:
            return second