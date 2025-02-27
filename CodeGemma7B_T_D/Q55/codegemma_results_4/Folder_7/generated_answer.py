def lists_with_product_equal_n(circular_list):
    """
  Returns a list of sublists such that the product of the integers in each sublist equals n.
  """
    sublists = []
    n = 24
    for i in range(len(circular_list)):
        product = circular_list[i]
        for j in range(1, len(circular_list)):
            if (i + j) % len(circular_list) == 0:
                break
            product *= circular_list[(i + j) % len(circular_list)]
            if product == n:
                sublists.append([circular_list[(i + k) % len(circular_list)] for k in range(j + 1)])
    return sublists