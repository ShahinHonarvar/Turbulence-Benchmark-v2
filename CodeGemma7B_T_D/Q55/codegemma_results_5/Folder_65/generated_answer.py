from itertools import islice

def lists_with_product_equal_n(intlist):
    result = []
    for i in range(len(intlist)):
        current_product = 1
        current_sublist = []
        for j in range(i, len(intlist)):
            current_product *= intlist[j]
            current_sublist.append(intlist[j])
            if current_product > 46:
                break
            if current_product == 46:
                result.append(current_sublist)
                break
    return result