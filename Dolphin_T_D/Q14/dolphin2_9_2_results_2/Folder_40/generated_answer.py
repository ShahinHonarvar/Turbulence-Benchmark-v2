def find_second_smallest_num(lst):
    if len(lst) < 3:
        return None
    elif len(lst) == 3:
        return lst[2]
    else:
        s1 = min(lst[0], lst[1], lst[2])
        s2 = max(lst[0], lst[1], lst[2])
        for i in range(3, len(lst)):
            if lst[i] < s2 and lst[i] != s1:
                s2 = lst[i]
            elif lst[i] < s1:
                s2 = s1
                s1 = lst[i]
        return s2 if s2 != s1 else None