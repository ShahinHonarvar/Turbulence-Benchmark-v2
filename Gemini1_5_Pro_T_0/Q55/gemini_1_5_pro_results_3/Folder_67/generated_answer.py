def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for i in range(n):
        for j in range(i, n):
            sublist = circular_list[i:j + 1]
            if j - i + 1 < n:
                product = 1
                for x in sublist:
                    product *= x
                if product == 33:
                    result.append(sublist)
            else:
                sublist.extend(circular_list[0:n - i])
                product = 1
                for x in sublist:
                    product *= x
                if product == 33:
                    result.append(sublist)
    return result