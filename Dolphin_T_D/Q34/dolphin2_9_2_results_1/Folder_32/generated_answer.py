def find_original_set(*args):
    result = set([0])
    for s in args:
        for x in s:
            if x not in result:
                result.add(x)
    return result