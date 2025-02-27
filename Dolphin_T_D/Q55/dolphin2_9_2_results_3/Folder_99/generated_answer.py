import collections

def lists_with_product_equal_n(list_n):
    result = []
    circular_list = collections.deque(list_n + list_n[0:1])
    for i in range(len(list_n)):
        if i > 0:
            circular_list.rotate(-1)
        product = 1
        for j in range(len(list_n)):
            product *= circular_list[j]
            if product == 415:
                if len(list(circular_list)) > 1:
                    result.append(list(circular_list))
                product /= circular_list[-1]
    return result