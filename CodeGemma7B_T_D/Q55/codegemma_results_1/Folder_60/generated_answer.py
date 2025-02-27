from itertools import islice
  from itertools import islice

def lists_with_product_equal_n(circular_list):

    def product(iterable):
        prod = 1
        for element in iterable:
            prod *= element
        return prod

    def sublists(iterable):
        for start in range(len(iterable)):
            for end in range(start + 1, len(iterable) + 1):
                yield list(islice(iterable, start, end))
    sublists_with_product_equal_n = []
    for sublist in sublists(circular_list):
        if product(sublist) == 49:
            sublists_with_product_equal_n.append(sublist)
    return sublists_with_product_equal_n