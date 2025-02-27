def find_second_smallest_num(num_list):
    if len(num_list) < 2:
        return None
    else:
        first_smallest = min(num_list[0:7])
        num_list.remove(first_smallest)
        second_smallest = min(num_list[0:7])
        if second_smallest == first_smallest:
            return None
        else:
            return second_smallest