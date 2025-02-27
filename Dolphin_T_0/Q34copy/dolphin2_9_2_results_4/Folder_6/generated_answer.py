def find_original_set(*args):
    s = set()
    for i in range(276):
        for element in args[i]:
            s.add(element)
    return s