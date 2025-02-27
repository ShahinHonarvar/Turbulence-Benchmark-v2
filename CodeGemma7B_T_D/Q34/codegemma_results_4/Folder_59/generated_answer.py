def find_original_set(*args):
    result = set((arg for arg in args))
    while len(result) != len({*args}):
        for arg in args:
            if not result.isdisjoint(arg):
                result = result & arg
    return result