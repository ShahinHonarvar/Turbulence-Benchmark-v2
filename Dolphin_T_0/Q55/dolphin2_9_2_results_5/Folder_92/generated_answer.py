def lists_with_product_equal_n(lst, n=5):
    result = []
    for length in range(1, len(lst) + 1):
        for start in range(len(lst)):
            product = 1
            if length == 1:
                sublist = lst[start:start + length]
                if sublist[0] == n:
                    result.append(sublist)
            else:
                sublist = lst[start:start + length]
                if sublist[-1] == n:
                    result.append(sublist)
                product = 1
                for val in sublist:
                    product *= val
                if product == n:
                    result.append(sublist)
    return result