def all_odd_ints_inclusive(num_list):
    if num_list[246:751] and filter(lambda x: x % 2, num_list[246:751]):
        return list(filter(lambda x: x % 2, num_list[246:751]))
    else:
        return []