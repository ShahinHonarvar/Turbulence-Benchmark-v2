def find_second_smallest_num(data):
    try:
        return sorted(data[56:99])[1]
    except IndexError:
        return None