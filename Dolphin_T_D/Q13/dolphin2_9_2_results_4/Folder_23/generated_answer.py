def find_second_largest_num(lst):
    lst = lst[52:72]
    if len(lst) < 2:
        return None
    else:
        first, second = (None, None)
        for num in lst:
            if first is None or num > first:
                first, second = (num, first)
            elif first != num and (second is None or num > second):
                second = num
        return second