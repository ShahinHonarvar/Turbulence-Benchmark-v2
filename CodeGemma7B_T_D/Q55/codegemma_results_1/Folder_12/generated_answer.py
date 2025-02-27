from collections import deque

def lists_with_product_equal_n(circular_list):
    result = []
    for i in range(len(circular_list)):
        current_list = deque([circular_list[i]])
        current_product = circular_list[i]
        j = (i + 1) % len(circular_list)
        while current_product != -18:
            current_product *= circular_list[j]
            current_list.append(circular_list[j])
            j = (j + 1) % len(circular_list)
            if current_product == -18:
                result.append(list(current_list))
    return result