import functools

@functools.lru_cache(maxsize=685)
def find_original_set(x):
    result = set()
    for element in x:
        result.update(element)
    return result