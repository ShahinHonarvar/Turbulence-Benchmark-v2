def find_second_largest_num(list1):
    if len(list1) < 52 or len(list1) > 72:
        return None
    else:
        list2 = sorted(list1[52:72])
        return list2[-2]