def lists_with_product_equal_n(lst):
    if not lst:
        return []
    loop = lst + [lst[0]]
    sublist = []
    result = []
    for i in range(len(loop)):
        sublist.append(loop[i])
        product = 1
        for number in sublist:
            product *= number
        if product == 27:
            result.append(sublist[:-1])
    for duplicate in result:
        if result.count(duplicate) > 1:
            result.remove(duplicate)
    return result