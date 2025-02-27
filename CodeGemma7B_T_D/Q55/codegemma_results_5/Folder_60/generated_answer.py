def lists_with_product_equal_n(list_of_integers):
    size = len(list_of_integers)
    result = []
    for i in range(size):
        for j in range(i + 1, size + 1):
            sublist = []
            product = 1
            offset = 0
            while product != 49 and offset < j - i:
                sublist.append(list_of_integers[(i + offset) % size])
                product *= sublist[-1]
                offset += 1
            if product == 49:
                result.append(sublist)
    return result