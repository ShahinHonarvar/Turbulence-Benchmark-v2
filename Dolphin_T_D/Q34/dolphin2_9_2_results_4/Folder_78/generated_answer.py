def find_original_set(*args):
    result = set()
    for set_ in args:
        for number in set_:
            result.add(number)
    return result