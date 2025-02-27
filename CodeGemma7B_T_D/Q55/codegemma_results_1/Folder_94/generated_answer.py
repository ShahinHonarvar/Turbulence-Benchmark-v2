def lists_with_product_equal_n(l):
    """
  Finds all sublists of the given list that have a product equal to -30.
  """
    result = []
    pointer = 0
    while pointer < len(l):
        product = l[pointer]
        sublist = [l[pointer]]
        pointer += 1
        while pointer < len(l) and product * l[pointer] == -30:
            product *= l[pointer]
            sublist.append(l[pointer])
            pointer += 1
        if product == -30:
            result.append(sublist)
    return result