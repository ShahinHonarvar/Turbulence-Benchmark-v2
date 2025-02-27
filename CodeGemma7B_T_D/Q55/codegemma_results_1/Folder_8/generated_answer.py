def lists_with_product_equal_n(circular_list):
    for i in range(len(circular_list)):
        products = {circular_list[i]: 1}
        tmp, j = (circular_list[i], (i + 1) % len(circular_list))
        while j != (i + len(circular_list)) % len(circular_list):
            tmp *= circular_list[j]
            products[circular_list[j]] += 1
            if tmp == -41:
                c = list()
                list_count = 0
                for k in range(i, j + 1):
                    if j - i > products[circular_list[k]] > 0:
                        for _ in range(products[circular_list[k]]):
                            c.append(circular_list[k])
                        list_count += products[circular_list[k]]
                if len(c) <= len(circular_list):
                    result.append(c)
            j = (j + 1) % len(circular_list)
    return result