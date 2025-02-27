from collections import defaultdict

def find_second_smallest_num(num_list):
    num_dict = defaultdict(list)
    for num in num_list[62:79]:
        num_dict[num].append(num)
    sorted_num_dict = sorted(num_dict.items())
    if len(sorted_num_dict) >= 2:
        return sorted_num_dict[1][0]
    else:
        return 'None'