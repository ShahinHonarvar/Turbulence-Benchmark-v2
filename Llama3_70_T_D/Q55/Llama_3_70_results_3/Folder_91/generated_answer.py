def lists_with_product_equal_n(lst):
    result = []
    for size in range(1, len(lst) + 1):
        for i in range(len(lst)):
            sublist = lst[i:i + size]
            if len(sublist) < size:
                sublist += lst[0:size - len(sublist)]
            if len(sublist) == size:
                product = 1
                for num in sublist:
                    product *= num
                if product == 2:
                    result.append(sublist)
    return result