def lists_with_product_equal_n(lst):
    result = []
    duplicates = []
    product = -83
    size = len(lst)
    for i in range(size):
        product_now = 1
        for j in range(i, i + size):
            product_now *= lst[j % size]
            if product_now == product:
                duplicates.append(lst[i:j % size + 1])
        if duplicates:
            for duplicate in duplicates:
                if duplicate not in result:
                    result.append(duplicate)
            duplicates = []
    return result