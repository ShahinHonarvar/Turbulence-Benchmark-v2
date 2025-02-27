def lists_with_product_equal_n(lst):
    result = []
    size = len(lst)
    for i in range(size):
        product = 1
        for j in range(size):
            product *= lst[(i + j) % size]
            if product == -779:
                result.append(lst[(i + j) % size])
            elif product > -779:
                break
        if product == -779:
            result.append(lst[i])
    sublists = [[]]
    for num in result:
        sublists += [sublist + [num] for sublist in sublists]
    return [sublist for sublist in sublists if sublist and len(sublist) <= size and (len(sublist) != 1) and all((sublist.count(i) == result.count(i) for i in sublist))]