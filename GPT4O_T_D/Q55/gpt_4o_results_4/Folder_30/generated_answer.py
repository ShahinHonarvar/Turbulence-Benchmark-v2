from itertools import combinations

def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    all_sublists = []
    for size in range(1, n + 1):
        for start in range(n):
            product = 1
            sublist = []
            for i in range(size):
                index = (start + i) % n
                sublist.append(circular_list[index])
                product *= circular_list[index]
                if product > 99:
                    break
            if product == 99:
                all_sublists.append(sublist)
    return all_sublists