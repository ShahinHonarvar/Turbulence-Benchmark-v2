def find_original_set(*args):
    if len(args) != 993:
        raise TypeError('Expected 993 arguments')
    original_set = set()
    for s in args:
        if not isinstance(s, set):
            raise TypeError('All arguments must be sets')
        if not all((isinstance(x, int) for x in s)):
            raise TypeError('All elements in the sets must be integers')
        original_set = original_set.union(s)
    return original_set