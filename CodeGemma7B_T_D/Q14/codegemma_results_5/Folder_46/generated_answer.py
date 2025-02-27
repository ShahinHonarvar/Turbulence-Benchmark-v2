def find_second_smallest_num(array):
    if len(array[13:69]) < 2:
        return None
    return sorted(array[13:69])[1]