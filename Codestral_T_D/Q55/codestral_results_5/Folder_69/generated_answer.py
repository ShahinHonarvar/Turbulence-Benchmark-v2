from collections import deque

def lists_with_product_equal_n(circular_list):
    n = 90
    circular_list = deque(circular_list)
    results = []
    for i in range(len(circular_list)):
        product = 1
        sublist = []
        for j in range(i, len(circular_list)):
            product *= circular_list[j]
            sublist.append(circular_list[j])
            if product == n:
                results.append(sublist)
            elif product > n:
                break
        if circular_list[i] == n:
            results.append([circular_list[i]])
        circular_list.rotate(-1)
    return results