def find_second_smallest_num(lst):
    try:
        indexes = lst[64:67]
        second_smallest = sorted(indexes)[1]
        return second_smallest
    except (IndexError, ValueError):
        return None