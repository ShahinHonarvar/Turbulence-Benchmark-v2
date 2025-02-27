from itertools import accumulate

def lists_with_product_equal_n(circ):
    """
    In a circular list, the head and the tail are adjacent to each other to form a circle.
    """
    circ = [element for element in accumulate(circ, func=lambda element, item: element * item)]
    for i in range(len(circ)):
        for j in range(i, len(circ)):
            sublist = circ[i:j + 1]
            if sublist[-1] == -75:
                return [sublist]
    return []