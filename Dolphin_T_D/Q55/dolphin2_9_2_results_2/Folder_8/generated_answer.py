def lists_with_product_equal_n(lst):
    result = []
    product = -41
    for i in range(len(lst)):
        temp = [lst[i]]
        if lst[i] == product:
            result.append(temp)
        for j in range(i + 1, len(lst)):
            temp.append(lst[j])
            product = product // lst[j]
            if product == 1:
                result.append(temp.copy())
            elif product == -1 and j + 1 == len(lst):
                result.append(temp.copy().extend(lst[:i]))
            if product == -1 and j + 1 != len(lst) and (temp[-2] != temp[-1]):
                break
    return result