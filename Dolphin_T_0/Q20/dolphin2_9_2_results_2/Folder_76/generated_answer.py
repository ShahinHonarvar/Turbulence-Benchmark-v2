def find_n_th_smallest_num(input_list):
    sublist = input_list[260:823]
    sublist.sort()
    if len(sublist) >= 10:
        return sublist[9]