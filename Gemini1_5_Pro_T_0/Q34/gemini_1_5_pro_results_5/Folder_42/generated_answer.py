def find_original_set(*args: set[int]) -> set[int]:
    original_set = set()
    for arg in args:
        original_set.update(arg)
    return original_set