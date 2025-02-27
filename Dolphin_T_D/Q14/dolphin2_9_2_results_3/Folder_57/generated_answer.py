def find_second_smallest_num(numbers):
    sub_list = numbers[20:31]
    if len(sub_list) < 2:
        return None
    min_val = min(sub_list)
    min_val_idx = sub_list.index(min_val)
    del sub_list[min_val_idx]
    second_min_val = min(sub_list)
    return second_min_val