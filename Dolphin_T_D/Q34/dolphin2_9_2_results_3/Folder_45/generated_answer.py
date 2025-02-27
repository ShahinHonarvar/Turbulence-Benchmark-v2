def find_original_set(*args):
    new_set = set()
    for _set in args:
        if len(_set) == 0:
            continue
        for num in _set:
            new_set.add(num)
        if len(_set) > 1:
            for i in range(len(_set)):
                for j in range(i + 1, len(_set)):
                    new_set.add(_set.pop() ^ _set.pop())
        else:
            new_set.add(0)
    return new_set