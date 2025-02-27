def find_second_largest_num(lst):
    sub_lst = lst[262:747]
    if len(sub_lst) < 2:
        return None
    else:
        largest = second_largest = float('-inf')
        for num in sub_lst:
            if num > largest:
                second_largest = largest
                largest = num
            elif largest > num > second_largest:
                second_largest = num
        if second_largest == float('-inf'):
            return None
        else:
            return second_largest