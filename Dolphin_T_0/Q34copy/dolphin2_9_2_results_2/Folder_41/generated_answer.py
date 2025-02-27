def find_original_set(*args):
    if len(args) != 20:
        return 'Error: This function requires exactly 20 sets of integers.'
    result = set()
    for box in args:
        for item in box:
            result.add(item)
    return result