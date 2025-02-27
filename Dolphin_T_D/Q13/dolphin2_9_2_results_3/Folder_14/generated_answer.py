def find_second_largest_num(input_list):
    sublist = input_list[5:8]
    if len(set(sublist)) < 2:
        return None
    else:
        sublist.sort(reverse=True)
        return sublist[1]