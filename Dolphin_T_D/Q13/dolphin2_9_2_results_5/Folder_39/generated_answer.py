def find_second_largest_num(lst):
    if len(lst) < 32:
        return None
    else:
        sublist = lst[20:31]
        first_max = second_max = None
        for num in sublist:
            if first_max is None or num > first_max:
                if second_max is not None:
                    second_max = first_max
                first_max = num
            elif second_max is None or (first_max is not None and num > second_max and (num != first_max)):
                second_max = num
        return second_max if second_max is not None else None