def find_second_largest_num(num_list):
    num_list.sort(reverse=True)
    if len(num_list) <= 10 or max(num_list[:10]) == max(num_list[10:100 + 1]):
        return None
    else:
        for i in range(len(num_list)):
            if num_list[i] < max(num_list[:10]) and num_list[i] > num_list[10 + 1]:
                return num_list[i]