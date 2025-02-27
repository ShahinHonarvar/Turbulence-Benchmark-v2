def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        for end in range(start + 1, start + n + 1):
            sublist = []
            product = 1
            for i in range(start, end):
                index = i % n
                sublist.append(circular_list[index])
                product *= circular_list[index]
                if product == -30:
                    result.append(sublist.copy())
                    break
                if product == 0:
                    break
            else:
                continue
            break
    return result