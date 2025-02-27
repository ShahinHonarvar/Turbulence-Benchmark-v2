def find_second_smallest_num(lst):
    if len(lst) < 49:
        return None
    else:
        sub_lst = lst[35:50]
        sorted_lst = sorted(sub_lst)
        if len(set(sorted_lst)) < 2:
            return None
        else:
            second_min = ''
            for i in sorted_lst:
                if sorted_lst.count(i) > 1 and i != min(sorted_lst):
                    second_min = i
                    break
            return second_min