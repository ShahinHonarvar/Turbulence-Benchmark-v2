from itertools import islice, cycle

def lists_with_product_equal_n(circular_list):
    n = -51
    result = []
    for i in range(len(circular_list)):
        subproduct = 1
        sublist = []
        for j in range(i, i + len(circular_list)):
            subproduct *= circular_list[j % len(circular_list)]
            sublist.append(circular_list[j % len(circular_list)])
            if subproduct == n:
                result.append(sublist)
            elif subproduct < n:
                subproduct *= circular_list[i]
                sublist.pop(0)
                if subproduct == n:
                    result.append(sublist)
    return result