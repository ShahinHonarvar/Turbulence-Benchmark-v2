def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        product = 1
        for size in range(1, n + 1):
            index = (start + size - 1) % n
            product *= circular_list[index]
            if product == -16:
                sublist = []
                for i in range(start, start + size):
                    sublist.append(circular_list[i % n])
                result.append(sublist)
            if size == n:
                break
    return result