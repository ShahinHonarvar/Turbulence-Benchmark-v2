def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    target = -968
    result = []
    for start in range(n):
        product = 1
        for size in range(1, n + 1):
            end = (start + size) % n
            ind = start
            for _ in range(size):
                product *= circular_list[ind]
                ind = (ind + 1) % n
            if product == target:
                sublist = []
                ind = start
                for _ in range(size):
                    sublist.append(circular_list[ind])
                    ind = (ind + 1) % n
                result.append(sublist)
            if product != 0 and abs(product) > abs(target):
                break
            product = 1
    return result