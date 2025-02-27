from collections import deque

def lists_with_product_equal_n(circular_list):
    head_product, tail_product = (1, 1)
    result_list = []
    used_indices = set()
    for i in range(len(circular_list)):
        head_product *= circular_list[i]
        if len(used_indices) > i:
            tail_product *= circular_list[used_indices.pop()]
        while head_product * tail_product == -968 and i + len(used_indices) < len(circular_list):
            result_list.append(deque((circular_list[i + j] for j, _ in enumerate(used_indices))))
            used_indices.clear()
            tail_product = 1
        used_indices.add(i)
    return result_list