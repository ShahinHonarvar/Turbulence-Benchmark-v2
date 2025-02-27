from itertools import product
from math import prod

def lists_with_product_equal_n(circular_list):

    def is_valid(sublist):
        return sublist and prod(sublist) == 733

    def sublists(seq, length):
        return (seq[i:i + length] for i in range(len(seq) - length + 1))
    seen = set()
    for length in range(1, len(circular_list) + 1):
        for sublist in sublists(circular_list, length):
            if is_valid(sublist) and sublist not in seen:
                seen.add(sublist)
                yield sublist