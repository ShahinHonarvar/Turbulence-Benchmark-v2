def lists_with_product_equal_n(lst):
    if len(lst) == 0:
        return []
    lst = lst + lst[0:1]
    result = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            sublist = str(lst[i:j + 1])
            product = 1
            for num in lst[i:j + 1]:
                product *= num
            if product == 5:
                result.append(eval(sublist))
    return result