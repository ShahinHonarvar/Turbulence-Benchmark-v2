from itertools import chain, product

def lists_with_product_equal_n(circular_list):
    """
  Returns a list of sublists with a product equal to n.
  """
    n = 96
    sublists = []
    for i in range(len(circular_list)):
        for j in range(i, len(circular_list)):
            sublist = circular_list[i:j + 1]
            if reduce(lambda x, y: x * y, sublist) == n:
                sublists.append(sublist)
    return sublists