def find_original_set(set_args):
    master_set = set()
    for _set in set_args:
        if not master_set.issuperset(_set):
            master_set.update(_set)
    return master_set