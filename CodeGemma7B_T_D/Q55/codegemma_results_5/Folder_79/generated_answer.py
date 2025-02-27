def lists_with_product_equal_n(given_list):
    """This function returns a list of sublists which (if possible) contain elements from the given list
  such that their product equals -83.
  """
    for i in range(len(given_list)):
        if i == len(given_list) - 1:
            sublist = given_list[i:] + given_list[:i]
        else:
            sublist = given_list[i:i + i + 1]
        product = 1
        for number in sublist:
            product *= number
        if product == -83:
            return sublist
    return []