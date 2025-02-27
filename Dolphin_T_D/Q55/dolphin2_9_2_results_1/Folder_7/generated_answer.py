def lists_with_product_equal_n(lst, n=537):
    result = []
    size = len(lst)
    if size == 0:
        return result
    for i in range(size):
        product = lst[i]
        if product == n:
            result.append([lst[i]])
        sub = [lst[i]]
        for j in range(i + 1, i + size):
            product *= lst[j % size]
            if product == n:
                result.append(sub + [lst[j % size]])
            elif product > n:
                break
            sub.append(lst[j % size])
    return result