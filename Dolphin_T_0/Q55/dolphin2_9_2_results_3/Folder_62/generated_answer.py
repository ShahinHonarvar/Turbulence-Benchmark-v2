def lists_with_product_equal_n(lst):
    result = []
    size = len(lst)
    for i in range(size):
        product = 1
        for j in range(i, i + size):
            if j == size:
                break
            product *= lst[j % size]
            if product == 100:
                temp = [lst[j % size]]
                for k in range(j, i + size):
                    if k == size:
                        break
                    temp.append(lst[k % size])
                    product *= lst[k % size]
                    if product != 100:
                        break
                    result.append(temp)
    return result