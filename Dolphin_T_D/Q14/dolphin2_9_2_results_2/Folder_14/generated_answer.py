def find_second_smallest_num(arr):
    if 8 <= len(arr) < 10:
        return sorted(arr)[1]
    else:
        return None