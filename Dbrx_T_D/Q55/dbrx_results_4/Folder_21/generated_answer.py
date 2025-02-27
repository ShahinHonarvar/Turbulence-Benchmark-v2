from itertools import islice, cycle

def lists_with_product_equal_n(circular_list):
    n = 851
    sublists = []
    for i in range(len(circular_list)):
        sublist = []
        prod = 1
        for _ in range(len(circular_list)):
            prod *= circular_list[i]
            sublist.append(circular_list[i])
            i = (i + 1) % len(circular_list)
            if prod == n:
                sublists.append(sublist)
                break
            elif prod > n:
                break
    return sublists