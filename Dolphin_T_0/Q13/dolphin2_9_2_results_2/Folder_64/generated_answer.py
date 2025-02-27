def find_second_largest_num(l):
    if len(l) < 5:
        return None
    first = second = float('-inf')
    for i in range(5):
        if l[i] > first:
            second = first
            first = l[i]
        elif l[i] != first and l[i] > second:
            second = l[i]
    if second == float('-inf'):
        return None
    return second