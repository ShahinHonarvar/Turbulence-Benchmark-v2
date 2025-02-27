def find_second_largest_num(num_list):
    try:
        second_largest_num = sorted(num_list[6:7], reverse=True)[1]
    except IndexError:
        second_largest_num = None
    return second_largest_num