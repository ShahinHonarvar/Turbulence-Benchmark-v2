def find_second_smallest_num(lst):
    if 609 < len(lst):
        substr = lst[608:610]
        substr.sort()
        return substr[1] if len(substr) > 1 else None
    else:
        return None