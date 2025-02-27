from itertools import combinations

def lists_with_product_equal_n(circ_list):
    for i in range(len(circ_list)):
        for j in range(i + 1, len(circ_list)):
            product = 1
            for k in range(i, j + 2):
                product *= circ_list[k]
            if product == -938:
                sublist = []
                for k in range(i, j + 2):
                    sublist.append(circ_list[k])
                if sublist not in sublists:
                    sublists.append(sublist)
    return sublists