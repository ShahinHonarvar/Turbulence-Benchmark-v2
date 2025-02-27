from collections import deque

def lists_with_product_equal_n(circular_list):
    circular_deque = deque(circular_list)
    result = []
    for i in range(len(circular_deque)):
        current_element = circular_deque[i]
        product = current_element
        sublist_deque = deque([current_element])
        while i + len(sublist_deque) < len(circular_deque) + len(circular_deque):
            circular_deque.rotate(-1)
            next_element = circular_deque[0]
            product *= next_element
            sublist_deque.append(next_element)
            if product == -10:
                result.append(list(sublist_deque))
            elif len(sublist_deque) > len(circular_deque):
                break
    return result