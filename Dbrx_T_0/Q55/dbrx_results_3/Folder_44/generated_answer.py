from itertools import islice, cycle

def circular_list(lst):
    return list(islice(cycle(lst), len(lst)))