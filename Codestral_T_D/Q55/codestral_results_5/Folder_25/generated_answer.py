def lists_with_product_equal_n(lst):
    n = -32
    result = []
    for i in range(len(lst)):
        if lst[i] == n:
            result.append([lst[i]])
        else:
            product = lst[i]
            temp = [lst[i]]
            for j in range(i + 1, len(lst) + i):
                if product == n:
                    result.append(temp)
                    break
                elif j < len(lst):
                    product *= lst[j]
                    temp.append(lst[j])
                else:
                    product *= lst[j - len(lst)]
                    temp.append(lst[j - len(lst)])
    return result