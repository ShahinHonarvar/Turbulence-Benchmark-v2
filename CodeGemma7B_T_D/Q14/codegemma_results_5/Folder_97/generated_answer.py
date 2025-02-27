from operator import itemgetter

def find_second_smallest_num(num_list):
    try:
        return sorted(num_list[31:35])[1]
    except IndexError:
        return 'None'