def find_original_set(arg):
    if all(set(arg).issuperset(set(arg[0]))):
        return set(arg[0])
    else:
        return set()