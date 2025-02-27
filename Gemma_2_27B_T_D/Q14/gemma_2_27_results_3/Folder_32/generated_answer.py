def find_second_smallest_num(data):
    try:
        return sorted(data[32:36])[1]
    except:
        return None