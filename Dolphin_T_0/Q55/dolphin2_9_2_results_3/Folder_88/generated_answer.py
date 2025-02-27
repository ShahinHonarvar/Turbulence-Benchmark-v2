def product_sublists(circular_list, n):
    result = []
    for i in range(len(circular_list)):
        prods = [circular_list[i]]
        for j in range(i + 1, len(circular_list)):
            if len(prods) >= 1 and prods[-1] != 1:
                prods.append(prods[-1] * circular_list[j])
            if prods[-1] == n and len(prods) > 1:
                result.append(circular_list[i:j + 1])
    return result

def lists_with_product_equal_n(circular_list):
    return product_sublists(circular_list + [circular_list[0]], -56)