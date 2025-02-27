def lists_with_product_equal_n(lst):
    n = len(lst)
    if n == 0:
        return []
    elif n == 1:
        return [lst] if lst[0] == 54 else []
    else:
        res = []
        product = 1
        for i in range(n):
            product *= lst[i]
            if product == 54:
                tmp = [lst[i]]
                j = i + 1
                while j != i:
                    j = j % n
                    if lst[j] != 1 and 54 % lst[j] == 0:
                        tmp.append(lst[j])
                    if 54 // product == 1:
                        res.append(tmp)
                    if lst[j] != 1:
                        product *= lst[j]
                    else:
                        break
                    j += 1
        return res