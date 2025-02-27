def lists_with_product_equal_n(lst):
    target_product = -690
    result = []
    for i in range(len(lst)):
        current_product = 1
        for j in range(len(lst)):
            current_product *= lst[(i + j) % len(lst)]
            if current_product == target_product:
                result.append(lst[i:i + j + 1])
    return result