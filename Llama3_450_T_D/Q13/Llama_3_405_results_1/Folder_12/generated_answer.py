def find_second_largest_num(num_list):
    try:
        second_largest_num = sorted(set(num_list[14:65]), reverse=True)[1]
        return second_largest_num
    except IndexError:
        return None