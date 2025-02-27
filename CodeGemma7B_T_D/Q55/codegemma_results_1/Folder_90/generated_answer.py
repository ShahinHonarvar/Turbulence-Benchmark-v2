from itertools import permutations

def lists_with_product_equal_n(circular_list):
    product = -690
    sublists = []
    for i in range(len(circular_list)):
        sublist = []
        temp = circular_list[i]
        for j in range(i + 1, len(circular_list)):
            temp *= circular_list[j]
            sublist.append(circular_list[j])
            if temp == product:
                sublists.append(sublist)
        sublist.clear()
        temp = circular_list[i]
    return sublists