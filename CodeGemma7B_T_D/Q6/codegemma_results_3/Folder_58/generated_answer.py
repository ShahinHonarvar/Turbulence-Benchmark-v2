from itertools import dropwhile
        from itertools import islice

def all_neg_ints_exclusive(lst):
    return list(islice(dropwhile(lambda x: x >= 0, lst), 100))