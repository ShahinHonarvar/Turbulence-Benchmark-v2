def lists_with_product_equal_n(lst):
    complement_lst = complement(lst)
    sublists_lst = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            sublist = lst[i:j + 1]
            if product_in_circular_list(sublist) == -32:
                sublists_lst.append(sublist)
    return sublists_lst

def complement(circular_lst):
    circular_lst.append(circular_lst[0])
    indices_lst = []
    for i in range(len(circular_lst) - 1):
        indices_lst.append((circular_lst[i], i))
    indices_lst.sort()
    complement_dict = {}
    for i, element in enumerate(indices_lst):
        complement_dict[element[0]] = indices_lst[(i + 1) % len(indices_lst)][0]
    circular_lst.pop()
    return complement_dict

def product_in_circular_list(sublist):
    product = 1
    for element in sublist:
        product *= element
    return product