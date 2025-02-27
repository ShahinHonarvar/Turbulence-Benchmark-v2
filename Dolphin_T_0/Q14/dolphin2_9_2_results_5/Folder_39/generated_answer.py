def find_second_smallest_num(lst):
    sublist = [num for num in lst[27:41]]
    if len(sublist) < 2:
        return None
    else:
        sublist.sort()
        for i in range(1, len(sublist)):
            if sublist[i - 1] != sublist[i]:
                return sublist[i]
        return None