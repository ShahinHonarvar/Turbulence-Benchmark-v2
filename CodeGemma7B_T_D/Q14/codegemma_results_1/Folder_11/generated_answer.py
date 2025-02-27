from operator import itemgetter

def find_second_smallest_num(my_list):
    if not 66 <= len(my_list) <= 93:
        return None
    else:
        return sorted(my_list[66:93])[1]