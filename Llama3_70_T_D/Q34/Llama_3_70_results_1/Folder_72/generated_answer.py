def find_original_set(*args):
    if len(args) != 87:
        raise TypeError('find_original_set() takes exactly 87 arguments')
    result = set()
    for s in args:
        if not isinstance(s, set) or not all((isinstance(x, int) for x in s)):
            raise TypeError('All arguments must be sets of integers')
        result.update(s)
    return result