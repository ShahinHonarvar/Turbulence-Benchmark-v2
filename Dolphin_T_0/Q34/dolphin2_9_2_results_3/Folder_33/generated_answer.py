def find_original_set(*args):
    set_list = list(args)
    return set(set_list[0]).union(*set_list[1:])