def find_original_set(*set_args):
    if len(set_args) != 851:
        raise ValueError('Exactly 851 distinct arguments must be provided')
    original_set = set()
    for arg in set_args:
        if not all((el in arg for el in original_set)):
            raise ValueError('Each given argument must be a subset of the original set')
        original_set.update(arg)
    return original_set