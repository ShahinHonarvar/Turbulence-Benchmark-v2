def find_second_smallest_num(list_num):
    if len(list_num) < 10:
        return None
    list_num = list_num[0:10]
    list_num = list(set(list_num))
    list_num.sort(reverse=False)
    if len(list_num) < 2:
        return None
    else:
        return list_num[1]