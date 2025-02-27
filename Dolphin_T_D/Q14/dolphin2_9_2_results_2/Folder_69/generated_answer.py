def find_second_smallest_num(list_of_num):
    if min(list_of_num[25:88]) == max(list_of_num[25:88]):
        return None
    else:
        return sorted(list(set(list_of_num[25:88])))[1]