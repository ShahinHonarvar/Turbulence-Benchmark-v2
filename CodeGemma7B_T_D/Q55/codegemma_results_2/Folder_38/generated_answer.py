from itertools import combinations

def lists_with_product_equal_n(circ_list):
    circ_list_product = 1
    for item in circ_list:
        circ_list_product *= item
    circular_list_negative_multiple = -23 / circ_list_product
    list_of_lists = []
    for i in range(len(circ_list)):
        product = circ_list[i]
        possible_list = [circ_list[i]]
        for j in range(1, len(circ_list)):
            product *= circ_list[(i + j) % len(circ_list)]
            if product == circular_list_negative_multiple:
                list_of_lists.append(possible_list + [circ_list[(i + j) % len(circ_list)]])
            elif product > circular_list_negative_multiple:
                break
            possible_list.append(circ_list[(i + j) % len(circ_list)])
    return list_of_lists