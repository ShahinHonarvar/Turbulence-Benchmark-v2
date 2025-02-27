def find_original_set(*args):
    result_set = set()
    for argument in args:
        for num in argument:
            result_set.add(num)
    return result_set