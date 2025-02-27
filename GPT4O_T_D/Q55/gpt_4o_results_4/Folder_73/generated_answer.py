def lists_with_product_equal_n(circular_list):
    result = []
    n = len(circular_list)
    for start in range(n):
        for end in range(start + 1, start + n + 1):
            product = 1
            sublist = []
            for i in range(start, end):
                index = i % n
                product *= circular_list[index]
                sublist.append(circular_list[index])
                if product == 40:
                    result.append(sublist[:])
                    break
                if product > 40:
                    break
    return result