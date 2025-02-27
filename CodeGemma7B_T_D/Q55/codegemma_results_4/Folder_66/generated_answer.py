def lists_with_product_equal_n(lista):
    result = []
    n = len(lista)
    for i in range(n):
        product = lista[i]
        sublist = [lista[i]]
        j = (i + 1) % n
        while product == 78:
            if lista[j] == 0:
                break
            product *= lista[j]
            sublist.append(lista[j])
            j = (j + 1) % n
        if product == 78:
            result.append(sublist)
        product = 1
        sublist = []
        j = (i + n - 1) % n
        while product == 78:
            if lista[j] == 0:
                break
            product *= lista[j]
            sublist.append(lista[j])
            j = (j - 1 + n) % n
        if product == 78:
            result.append(sublist)
    return result