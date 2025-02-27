from itertools import combinations_with_replacement

def lists_with_product_equal_n(circular_list):
    circular_list.append(circular_list[0])
    lists = []
    for i in range(len(circular_list)):
        for j in range(i + 1, len(circular_list)):
            sublist = circular_list[i:j + 1]
            if product_of_sublist(sublist) == 733 and len(sublist) <= len(circular_list):
                lists.append(sublist)
    return lists

def product_of_sublist(sublist):
    product = 1
    for element in sublist:
        product *= element
    return product