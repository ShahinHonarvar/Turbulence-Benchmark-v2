def lists_with_product_equal_n(lst):
    n = 851
    result = []
    length = len(lst)
    for i in range(length):
        product = 1
        for j in range(i, i + length):
            product *= lst[j % length]
            if product == n:
                sublist = lst[i:j + 1]
                if i > j:
                    sublist = lst[i:] + lst[:j + 1]
                result.append(sublist)
            elif product > n:
                break
    return result