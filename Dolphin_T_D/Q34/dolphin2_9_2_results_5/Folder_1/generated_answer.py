def find_original_set(*args):
    result_set = set()
    for i in range(29):
        for integers in args[i]:
            result_set.add(integers)
    return result_set