from itertools import islice, cycle

def lists_with_product_equal_n(circular_list):
    n = -30
    result = []
    for i in range(len(circular_list)):
        sub_list = []
        current_product = 1
        for j in range(len(circular_list)):
            current_sub_list = sub_list[j:] if sub_list else [circular_list[(i + j) % len(circular_list)]]
            current_product *= current_sub_list[-1]
            if current_product == n:
                result.append(current_sub_list)
            elif current_product < n:
                sub_list.extend(current_sub_list[1:])
            elif current_product > n:
                break
    return result