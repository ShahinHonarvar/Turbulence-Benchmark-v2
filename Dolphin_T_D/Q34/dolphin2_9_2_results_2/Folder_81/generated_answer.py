def find_original_set(*args: set) -> set:
    result = set()
    for arg in args:
        result.update(arg)
    return result