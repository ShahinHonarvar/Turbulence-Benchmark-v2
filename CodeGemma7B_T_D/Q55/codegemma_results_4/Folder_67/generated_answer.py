def lists_with_product_equal_n(circular_list):
    """
            :param circular_list: a circular list of integers
            :return: a list of sublists of the given list such that
            the product of their elements equals 33.
            """
    sublists = []
    for i in range(len(circular_list)):
        curr_sublist = [circular_list[i]]
        for j in range(i + 1, len(circular_list)):
            product = 1
            for element in curr_sublist:
                product *= element
            if product == 33:
                sublists.append(curr_sublist)
            curr_sublist.append(circular_list[j])
    return sublists