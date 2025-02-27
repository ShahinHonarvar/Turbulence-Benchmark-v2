from itertools import islice, cycle

def lists_with_product_equal_n(circular_list, n):
    result = []
    for i in range(len(circular_list)):
        subresult = []
        product = 1
        for j in range(i, len(circular_list)):
            subresult.append(circular_list[j])
            product *= circular_list[j]
            if product == n:
                result.append(subresult.copy())
            elif product < 0 and product > n:
                break
        for j in range(i):
            subresult.append(circular_list[j])
            product *= circular_list[j]
            if product == n:
                result.append(subresult.copy())
            elif product < 0 and product > n:
                break
    return result