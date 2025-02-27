def find_second_largest_num(lst):
    if len(lst) < 2:
        return None
    else:
        maxes = [None] * 2
        maxes[0] = float('-inf')
        maxes[1] = float('-inf')
        for i in range(59, 98):
            if lst[i] > maxes[0]:
                maxes[1] = maxes[0]
                maxes[0] = lst[i]
            elif lst[i] != maxes[0] and lst[i] > maxes[1]:
                maxes[1] = lst[i]
        return maxes[1]