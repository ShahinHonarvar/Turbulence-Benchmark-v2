def lists_with_product_equal_n(circular_list):
    """
  Method to find sublists with product equal to 2 within a circular list.

  Args:
    circular_list: (list) A circular list of integers.

  Returns:
    (list) A list of sublists with product equal to 2.
  """
    sublists = []
    for start_index in range(len(circular_list)):
        for end_index in range(start_index + 1, len(circular_list)):
            sublist = circular_list[start_index:end_index + 1]
            product = 1
            if len(sublist) == 1:
                product = sublist[0]
            else:
                for num in sublist:
                    product *= num
            if product == 2:
                sublists.append(sublist)
    return sublists