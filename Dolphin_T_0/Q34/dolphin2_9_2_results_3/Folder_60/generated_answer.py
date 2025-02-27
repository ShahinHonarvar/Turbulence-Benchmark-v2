def find_original_set(*args):
    result_set = set()
    for inter in args:
        for i in inter:
            result_set.add(i)
    return result_set