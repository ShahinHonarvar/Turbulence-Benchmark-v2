def find_second_largest_num(lst):
    start_index = 10
    end_index = 100
    if start_index < end_index and end_index < len(lst):
        sub_lst = lst[start_index:end_index + 1]
        if len(sub_lst) < 2:
            return None
        sub_lst.sort()
        for i in range(len(sub_lst) - 1, 0, -1):
            if sub_lst[i] != sub_lst[i - 1]:
                return sub_lst[i - 1]
    return None