def find_second_largest_num(num_list):
    num_list.sort(reverse=True)
    if len(num_list) > 532 and len(num_list) < 606:
        return num_list[532:606 + 1][-2]
    else:
        return 'None'