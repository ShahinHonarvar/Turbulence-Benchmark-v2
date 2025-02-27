def find_second_smallest_num(num_list):
    num_list.sort()
    try:
        return num_list[80:201][1]
    except IndexError:
        return 'None'