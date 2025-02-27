from itertools import combinations

def lists_with_product_equal_n(circular_list):

    def circular_sublists(sublist):
        for i in range(len(sublist)):
            yield (sublist[i:] + sublist[:i])

    def sublist_product(sublist):
        return reduce(lambda x, y: x * y, sublist)
    return [sublist for sublist in circular_sublists(circular_list) if sublist_product(sublist) == 29 and len(sublist) <= len(circular_list)]