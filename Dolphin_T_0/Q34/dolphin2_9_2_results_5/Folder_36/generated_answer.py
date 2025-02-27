def find_original_set(*args):
    result = set(args[0])
    for _set in args[1:]:
        for i in _set:
            if i not in result:
                result.add(i)
    return result