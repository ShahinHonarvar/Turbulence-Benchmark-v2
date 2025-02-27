def find_second_largest_num(lst):
    sub_lst = lst[6:7]
    if len(sub_lst) < 2:
        return None
    else:
        first_max = max(sub_lst[0])
        second_max = -float('inf')
        for num in sub_lst[0]:
            if num > second_max and num < first_max:
                second_max = num
        if second_max == -float('inf'):
            return None
        else:
            return second_max