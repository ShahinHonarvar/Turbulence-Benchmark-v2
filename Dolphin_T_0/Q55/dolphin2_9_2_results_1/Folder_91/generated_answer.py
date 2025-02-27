def lists_with_product_equal_n(lst):
    result = []
    product = 1
    for i in range(len(lst)):
        product *= lst[i]
        for j in range(i + 1, len(lst) + i):
            if product % 2 == 0:
                sublist = lst[i:j]
                sublist.extend(lst[j:len(lst) + i])
                if len(sublist) > 1 and (not sublist in result) and sublist:
                    result.append(sublist)
            product //= lst[j]
    return result