from itertools import product

def lists_with_product_equal_n(array):
    final_result = []
    for a in range(len(array)):
        for b in range(a, len(array)):
            temp = array[a:b + 1]
            product_of_temp = 1
            for c in temp:
                product_of_temp *= c
            if product_of_temp == 733:
                final_result.append(temp)
    return final_result