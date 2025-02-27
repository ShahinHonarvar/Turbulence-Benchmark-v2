def find_second_smallest_num(lst):
    if 661 <= len(lst) <= 924:
        extracted = sorted(lst[661:924 + 1])
        if len(extracted) > 1:
            return extracted[1]
    return None