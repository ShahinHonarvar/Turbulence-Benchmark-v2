from itertools import islice, cycle

def circular_list_product(l, start, end):
    end = end % len(l) if end < 0 else end
    return reduce(lambda x, y: x * y, [l[i] for i in range(start, end + 1)])

def sublists_with_product_equal_n(l, n):

    def circular_sublists(l, k):
        for i in xrange(len(l)):
            yield tuple(islice(cycle(l), i, i + k))
    return [sl for sl in circular_sublists(l, k) for k in xrange(1, len(l) + 1) if circular_list_product(list(sl), 0, len(sl) - 1) == n]

def lists_with_product_equal_n(l):
    return filter(lambda x: x != [], [sublists_with_product_equal_n(list(permutations(l, k)), -44) for k in xrange(1, len(l) + 1)])