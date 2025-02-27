def lists_with_product_equal_n(lst):
    result = []
    if not lst or len(lst) < 1:
        return result
    total_product = 1
    current_product = 1
    current_sublist = []
    for i in range(len(lst)):
        total_product *= lst[i]
        current_product = total_product // lst[i]
        if current_product == 40:
            current_sublist.append(lst[i])
            result.append(current_sublist[:])
            current_sublist.clear()
        else:
            current_sublist.append(lst[i])
            if total_product > 40:
                current_sublist.clear()
    return result