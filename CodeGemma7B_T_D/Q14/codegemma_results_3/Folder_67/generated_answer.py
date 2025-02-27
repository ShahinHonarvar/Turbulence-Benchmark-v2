import sys

def find_second_smallest_num(num_list):
    is_sorted = True
    for i in range(1, len(num_list)):
        if num_list[i] < num_list[i - 1]:
            is_sorted = False
            break
    if is_sorted:
        if len(num_list) >= 55:
            return num_list[50:55]
        else:
            return 'None'
    min_num = min(num_list)
    num_list.remove(min_num)
    return min(num_list)