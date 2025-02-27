def find_original_set(*args):
    result = set()
    for set_num in args:
        for num in set_num:
            result.add(num)
    return result