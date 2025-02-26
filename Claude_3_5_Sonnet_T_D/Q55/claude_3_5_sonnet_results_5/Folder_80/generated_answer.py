def lists_with_product_equal_n(circular_list):
    n = 43
    result = []
    length = len(circular_list)
    for start in range(length):
        for end in range(length):
            sublist = []
            product = 1
            for i in range(start, start + length):
                index = i % length
                sublist.append(circular_list[index])
                product *= circular_list[index]
                if product == n:
                    result.append(sublist.copy())
                elif product > n:
                    break
                if i - start + 1 == length:
                    break
            if start == end:
                break
    return result