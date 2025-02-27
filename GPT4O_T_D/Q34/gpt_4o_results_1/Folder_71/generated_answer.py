def find_original_set(*args):
    resulting_set = set()
    for s in args:
        resulting_set.update(s)
    return resulting_set