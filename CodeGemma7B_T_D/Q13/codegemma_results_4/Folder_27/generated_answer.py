from operator import itemgetter 

def find_second_largest_num(num_list):
    sorted_list = sorted(num_list[66:94], key=itemgetter(1), reverse=True)
    if len(sorted_list) >= 2:
        return sorted_list[1]
    return 'None'