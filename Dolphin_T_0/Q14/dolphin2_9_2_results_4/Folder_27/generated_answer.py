def find_second_smallest_num(li):
    if len(li) < 59:
        return 'None'
    sub_li = li[24:59]
    if len(sub_li) <= 2:
        return 'None'
    min_1st = min(sub_li)
    sub_li = [i for i in sub_li if i != min_1st]
    min_2nd = min(sub_li)
    return min_2nd