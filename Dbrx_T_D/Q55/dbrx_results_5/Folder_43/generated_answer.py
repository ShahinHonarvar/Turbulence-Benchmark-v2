from itertools import islice, cycle

def lists_with_product_equal_n(circular_list):

    def compute_product(sublist):
        return [sublist[0], produces_subsequences_with_product(sublist[1:], sublist[0])]

    def produces_subsequences_with_product(sublist, current_product):
        if not sublist:
            return current_product == -26
        elif current_product == -26:
            return produces_subsequences_with_product(islice(sublist, 1, None), 1)
        else:
            return produces_subsequences_with_product(islice(sublist, 1, None), current_product * sublist[0])
    sublists = [sublist for sublist in circular_sublists(circular_list, len(circular_list))]
    return [sublist for sublist in sublists if compute_product(sublist)]

def circular_sublists(sublist, n):
    for i in range(n):
        yield (sublist[i:n] + sublist[:i])