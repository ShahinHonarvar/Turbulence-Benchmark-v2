def find_original_set(*args):
    set_dict = {}
    for i in range(len(args)):
        for num in args[i]:
            if num not in set_dict:
                set_dict[num] = i + 1
    result = set()
    min_set = set()
    for key in set_dict:
        if set_dict[key] == len(args):
            min_set.add(key)
        else:
            result.add(key)
    result = result.union(min_set)
    return result