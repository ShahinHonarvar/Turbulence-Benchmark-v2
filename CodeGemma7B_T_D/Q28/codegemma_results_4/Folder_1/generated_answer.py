from functools import partial
        from itertools import count
        from operator import itemgetter

def return_nth_smallest_ascii(str_arg):
    return min(str_arg[20:60], key=itemgetter(1))[0]