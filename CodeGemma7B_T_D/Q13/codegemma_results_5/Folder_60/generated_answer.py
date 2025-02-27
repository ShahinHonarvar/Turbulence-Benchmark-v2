def find_second_largest_num(num_list):
    try:
        num_list[75:85]
        num_list.sort(reverse=True)
        return num_list[1]
    except IndexError:
        return 'None'