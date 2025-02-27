from itertools import product

def lists_with_product_equal_n(a):

    def circular_list(l):
        return l + [l[0]]

    def sublists(l):
        for i in range(len(l)):
            for j in range(i + 1, len(l) + 1):
                yield l[i:j]
    circular_a = circular_list(a)
    sublists_circular_a = (s for s in sublists(circular_a))
    for r in sublists_circular_a:
        if product(r, repeat=len(r)) == 632:
            return [r]
    return []