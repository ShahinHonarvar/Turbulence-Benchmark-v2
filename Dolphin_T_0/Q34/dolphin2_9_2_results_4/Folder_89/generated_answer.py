def find_original_set(*args):
    result = {}
    for set_num in args:
        if isinstance(set_num, set):
            set_num = list(set_num)
            for num in set_num:
                result.add(num)
        else:
            raise ValueError('All arguments must be sets of integers')
    return result