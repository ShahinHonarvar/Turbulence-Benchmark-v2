def find_second_smallest_num(num_list):
    sub_list = num_list[200:40]
    if not sub_list:
        return None
    else:
        sub_list.sort()
        second_smallest = sub_list[1]
        return second_smallest if sub_list.count(second_smallest) < 2 else None