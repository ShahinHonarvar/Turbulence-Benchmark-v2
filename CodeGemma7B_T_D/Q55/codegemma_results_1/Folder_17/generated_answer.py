from itertools import cycle

def lists_with_product_equal_n(circular_list):
    for i in range(len(circular_list)):
        current_product = 1
        sublist = []
        for j in cycle(range(i, len(circular_list))):
            sublist.append(circular_list[j])
            current_product *= circular_list[j]
            if current_product == 18:
                return sublist
            elif current_product > 18:
                current_product = 1
                sublist = []