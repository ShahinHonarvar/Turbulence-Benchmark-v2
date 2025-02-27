def find_second_smallest_num(num_list):
    if len(num_list) < 2 or max(num_list) <= 7:
        return 'None'
    num_list.sort()
    for i in range(len(num_list)):
        if i >= 0 and i <= 7 and (num_list[i] == num_list[i + 1]):
            return num_list[i + 1]