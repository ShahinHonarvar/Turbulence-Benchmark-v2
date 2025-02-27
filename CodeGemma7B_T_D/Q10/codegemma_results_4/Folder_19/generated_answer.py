def all_odd_ints_exclusive(int_list):
    if all((not i % 2 for i in int_list[2:3])):
        return []
    return [i for i in int_list[2:6] if i % 2]