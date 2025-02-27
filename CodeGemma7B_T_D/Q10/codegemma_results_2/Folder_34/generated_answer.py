def all_odd_ints_exclusive(my_list):
    odd_ints = [x for x in my_list if x % 2 != 0 and 60 < x < 200]
    if not odd_ints:
        return []
    return odd_ints