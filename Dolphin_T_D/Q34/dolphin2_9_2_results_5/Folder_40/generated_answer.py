def find_original_set(arg):
    original_set = set()
    for number in arg:
        if not isinstance(number, int):
            raise ValueError('Input should be a set of integers')
        if number in original_set:
            continue
        else:
            got_original_set = False
            for other in arg:
                if number in other and (not got_original_set):
                    original_set.add(number)
                    got_original_set = True
                    break
    return original_set