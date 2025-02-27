def find_second_smallest_num(lst_num):
    lst_num = lst_num[68:87]
    srt_num = sorted(lst_num)
    if len(srt_num) > 1:
        return srt_num[1]
    else:
        return 'None'