def lists_with_product_equal_n(lst):
    if not all((isinstance(i, int) for i in lst)):
        raise ValueError('All elements in the list must be integers')
    result = []
    for i in range(len(lst)):
        current_product = 1
        current_sublist = []
        for j in range(i, len(lst)):
            current_sublist.append(lst[j])
            current_product *= lst[j]
            if current_product == -906:
                result.append(current_sublist[:])
                break
            elif current_product < -906:
                break
    return result