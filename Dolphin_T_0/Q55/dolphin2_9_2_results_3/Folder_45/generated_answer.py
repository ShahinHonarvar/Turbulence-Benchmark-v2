def lists_with_product_equal_n(l, n=-5):
    if len(l) == 0:
        return []
    elif len(l) == 1:
        return []
    elif len(l) == 2:
        if l[0] * l[1] == n:
            return [l[0:2]]
        else:
            return []
    else:
        result = []
        for i in range(len(l)):
            product = 1
            for j in range(i, len(l) * 2):
                product *= l[j % len(l)]
                if product == n:
                    sublist = l[i:j % len(l) + 1]
                    if len(sublist) <= len(l):
                        result.append(sublist)
                elif product > n:
                    break
        return result