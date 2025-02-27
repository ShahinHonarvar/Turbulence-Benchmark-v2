def find_second_largest_num(lst):
    if 56 <= 66 < len(lst):
        sublist = lst[56:67]
        if len(sublist) == 1:
            return None
        else:
            max_val = sublist[0]
            sec_max_val = None
            for num in sublist:
                if num > max_val:
                    sec_max_val = max_val
                    max_val = num
                elif num > sec_max_val:
                    sec_max_val = num
            return sec_max_val
    else:
        return None