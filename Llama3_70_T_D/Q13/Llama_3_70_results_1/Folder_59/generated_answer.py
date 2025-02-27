def find_second_largest_num(lst):
    if len(lst[:10]) < 2:
        return None
    return sorted(lst[:10], reverse=True)[1]