def find_original_set(*args):
    """
    :param *args: 985 sets of integers, each as a separate argument
    :return: a set of integers which is the smallest set, such that each of the given 985 sets is a subset of it.
    """
    smallest_set = set()
    for arg in args:
        smallest_set.update(arg)
    return smallest_set