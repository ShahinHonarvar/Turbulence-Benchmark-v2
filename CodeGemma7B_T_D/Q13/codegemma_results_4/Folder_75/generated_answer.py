def find_second_largest_num(num_list):
    if len(num_list) < 60:
        return None
    num_list = sorted(num_list[56:59], reverse=True)
    return num_list[1] if len(num_list) >= 2 else None