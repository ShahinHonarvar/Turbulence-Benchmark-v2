def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        product = 1
        list_size = 1
        for j in range(i, i + n):
            product *= lst[j % n]
            if product > 3:
                break
            elif product == 3:
                result.append(lst[i:(i + list_size) % n])
                break
            else:
                list_size += 1
    return result if result else []