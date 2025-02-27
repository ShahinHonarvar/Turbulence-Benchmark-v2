from itertools import islice, cycle

def lists_with_product_equal_n(circular_list):

    def sublists_with_product_equal_n(circular_list, target):
        sl = []
        for i in range(len(circular_list)):
            sub_circular_list = circular_list[i:] + circular_list[:i]
            product = 1
            sublist = []
            for j in range(len(sub_circular_list)):
                product *= sub_circular_list[j]
                sublist.append(sub_circular_list[j])
                if product == target:
                    sl.append(sublist)
                elif product > target:
                    break
        return sl
    return sublists_with_product_equal_n(circular_list, 49)