def lists_with_product_equal_n(lst):
    result = []
    product = 1
    for i in range(len(lst)):
        if i + 1 < len(lst):
            product *= lst[i]
            for j in range(i + 1, len(lst)):
                sublist = lst[i:j + 1]
                product *= lst[j]
                if product == 27:
                    result.append(sublist)
                elif product > 27:
                    break
                elif product < 27:
                    product -= lst[i]
    return result