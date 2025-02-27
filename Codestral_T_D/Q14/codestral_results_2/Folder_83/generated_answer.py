def find_second_smallest_num(lst):
    if 90 <= len(lst) <= 200:
        sub_lst = sorted(lst[90:201])
        smallest = sub_lst[0]
        for num in sub_lst:
            if num > smallest:
                return num
    return None