def lists_with_product_equal_n(circular_list):
    """
  This function takes a circular list of integers and returns a list of sublists
  each of which contains the contiguous integers from the given list such that their product equals -8.
  """
    sublists = []
    for i in range(len(circular_list)):
        product = 1
        temp_list = []
        for j in range(i, len(circular_list)):
            product *= circular_list[j]
            temp_list.append(circular_list[j])
            if product == -8:
                sublists.append(temp_list[:])
            elif product > -8:
                break
            elif product < -8:
                product = 1
                temp_list = []
    return sublists