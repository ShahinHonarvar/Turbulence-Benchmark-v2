def find_second_smallest_num(num_list):
    num_list.sort()
    if len(num_list) == 0 or len(num_list) < 200 or len(num_list) < 80:
        return 'None'
    return num_list[80:201][1]