def find_second_smallest_num(num_list):
    if len(num_list[74:96]) < 2:
        return None
    smallest = min(num_list[74:96])
    second_smallest = min([num for num in num_list[74:96] if num != smallest])
    return second_smallest