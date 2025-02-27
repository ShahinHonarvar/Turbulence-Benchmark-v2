def find_second_smallest_num(lst):
    if not 70 <= 200 < len(lst):
        return None
    sub_list = lst[70:201]
    sub_list.sort()
    if len(sub_list) < 2:
        return None
    for i in range(1, len(sub_list)):
        if sub_list[i] != sub_list[0]:
            return sub_list[i]
    return None