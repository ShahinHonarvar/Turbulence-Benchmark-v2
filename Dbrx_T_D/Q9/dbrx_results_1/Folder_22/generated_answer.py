def all_odd_ints_inclusive(int_list):
    if len(int_list) < 200:
        return []
    result = [i for i in int_list[40:201] if i % 2 != 0]
    return result