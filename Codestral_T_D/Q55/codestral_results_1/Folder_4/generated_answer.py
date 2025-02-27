from collections import deque

def lists_with_product_equal_n(circular_list):
    n = 91
    size = len(circular_list)
    result = []
    circular_list *= 2
    for i in range(size):
        for j in range(i + 1, i + size):
            product = 1
            sublist = deque()
            for k in range(i, j + 1):
                product *= circular_list[k]
                sublist.append(circular_list[k])
                if product > n:
                    break
                if product == n:
                    result.append(list(sublist))
    return result