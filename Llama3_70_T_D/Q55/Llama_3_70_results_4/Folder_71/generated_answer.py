def lists_with_product_equal_n(lst):
    result = []
    size = len(lst)
    for i in range(size):
        current_product = 1
        for j in range(size):
            current_product *= lst[(i + j) % size]
            if current_product == 47:
                if sorted(lst[i:i + j + 1]) not in [sorted(sublist) for sublist in result]:
                    result.append(lst[i:i + j + 1])
            elif current_product > 47:
                break
    return result