def find_second_smallest_num(num_list):
    if len(num_list) < 10:
        return None
    else:
        first_smallest = min(num_list[:10])
        second_smallest = min((i for i in num_list[:10] if i != first_smallest))
        return second_smallest