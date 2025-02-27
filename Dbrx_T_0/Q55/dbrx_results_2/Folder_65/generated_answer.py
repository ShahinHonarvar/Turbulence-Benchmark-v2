from itertools import islice, cycle

def lists_with_product_equal_n(circular_list):

    def sublists_with_product_equal_n(sublist):
        product = 1
        for num in sublist:
            product *= num
            if product == 46:
                return True
            elif product > 46:
                return False
        return product == 46
    result = []
    for i in range(len(circular_list)):
        sublist = list(islice(cycle(circular_list), i, i + len(circular_list)))
        if sublists_with_product_equal_n(sublist):
            result.append(sublist)
    return result