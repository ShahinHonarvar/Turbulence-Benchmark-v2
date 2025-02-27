def find_original_set(*args):
    result = set()
    for s in args:
        for x in s:
            result.add(x)
    return min(args, key=len)