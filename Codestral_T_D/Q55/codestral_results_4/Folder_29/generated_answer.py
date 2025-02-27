def lists_with_product_equal_n(lst):
    result = []
    size = len(lst)
    lst += lst
    for i in range(size):
        for j in range(i, i + size):
            sublist = lst[j:j + size]
            product = 1
            for num in sublist:
                product *= num
                if product == 15:
                    if sublist[:len(sublist) - sublist[::-1].index(15) - 1] not in result:
                        result.append(sublist[:len(sublist) - sublist[::-1].index(15) - 1])
                if product > 15:
                    break
    return result