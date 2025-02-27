from functools import reduce

def lists_with_product_equal_n(circular_list):
    current_idx = 0
    result = []
    while current_idx < len(circular_list):
        product = circular_list[current_idx]
        current_idx += 1
        for next_idx in range(current_idx, len(circular_list)):
            product *= circular_list[next_idx]
            if product == 0:
                sublist = circular_list[current_idx:next_idx + 1]
                result.append(sublist)
                current_idx = next_idx + 1
                break
            elif next_idx + 1 == len(circular_list):
                current_idx = 0
                break
    return result