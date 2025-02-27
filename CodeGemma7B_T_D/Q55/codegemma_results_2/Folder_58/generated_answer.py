from itertools import izip_longest

def lists_with_product_equal_n(circular_list):
    """Circular list members is an extension of class list"""
    size = len(circular_list)
    result = []
    for i in xrange(size):
        for j in xrange(i, size):
            product = 1
            for k, (a, b) in enumerate(izip_longest(circular_list[i:], [circular_list[i]] * max(j - i, 0), circular_list[i:j + 1])):
                if a and b:
                    product *= a * b
            if product == 733:
                sublist = circular_list[i:j + 1]
                if sublist not in result:
                    result.append(sublist)
    return result