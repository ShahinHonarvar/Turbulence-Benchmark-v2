from functools import reduce

def lists_with_product_equal_n(circular_list):
    """
            Given a circular list of integers, return a list of sublists such that their product equals 46.

            Parameters:
                circular_list: A circular list of integers.

            Returns:
                A list of sublists with the product of their elements equal to 46.
            """

    def multiply(x, y):
        return x * y
    product = reduce(multiply, circular_list)
    if product % 46 != 0:
        return []
    sublists = []
    for i in range(len(circular_list)):
        for j in range(i + 1, len(circular_list)):
            sublist = circular_list[i:j + 1]
            if reduce(multiply, sublist) == 46:
                sublists.append(sublist)
    return sublists