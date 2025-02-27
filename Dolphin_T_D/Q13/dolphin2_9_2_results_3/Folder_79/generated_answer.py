def find_second_largest_num(lst):
    if len(lst) < 5:
        return None
    st = set(lst[4:5])
    if len(st) != 1:
        return None
    st.remove(max(st))
    if len(st) == 0:
        return None
    return list(st)[0]