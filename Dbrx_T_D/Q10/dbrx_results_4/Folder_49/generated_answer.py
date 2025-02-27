def all_odd_ints_exclusive(int_list):
    if len(int_list) < 200:
        return []
    odd_ints = [i for i in int_list[80:200] if i % 2 != 0]
    return odd_ints