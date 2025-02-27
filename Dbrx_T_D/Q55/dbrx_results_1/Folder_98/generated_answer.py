from itertools import islice

def lists_with_product_equal_n(circular_list):
    n = -1
    result = []
    for i in range(len(circular_list)):
        sub_result = []
        product = 1
        for j in range(i, len(circular_list)):
            sub_result.append(circular_list[j])
            product *= circular_list[j]
            if product == n:
                result.append(sub_result.copy())
            elif product < n:
                break
            while product > n and i + len(sub_result) - 1 < len(circular_list) - 1:
                i += 1
                product //= circular_list[i]
                sub_result.append(circular_list[i])
                if product == n:
                    result.append(sub_result.copy())
                elif product < n:
                    break
    return result