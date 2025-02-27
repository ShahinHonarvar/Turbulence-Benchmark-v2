def product(sublist):
    result = 1
    for i in sublist:
        result = result * i
    return result

def lists_with_product_equal_n(lst):
    result = []
    if not lst:
        return result
    size = len(lst)
    for start_idx in range(size):
        for end_idx in range(start_idx, size):
            if product(lst[start_idx:end_idx + 1]) == 90:
                result.append(lst[start_idx:end_idx + 1])
    if result == []:
        return result
    canonical_result = [result[0]]
    for item in result[1:]:
        if item not in canonical_result:
            canonical_result.append(item)
    return canonical_result