from itertools import islice, cycle

def lists_with_product_equal_n(lst):

    def circular_sublists(lst):
        return [list(islice(cycle(lst), i, i + len(sublist))) for i, sublist in enumerate(itertools.product([-69], repeat=len(lst)))]
    return [sublist for sublist in circular_sublists(lst) if all((x in lst for x in sublist)) and (not all((x == -69 for x in sublist)))]