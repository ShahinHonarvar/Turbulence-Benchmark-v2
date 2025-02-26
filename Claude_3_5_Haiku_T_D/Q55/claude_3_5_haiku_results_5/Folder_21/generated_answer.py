def lists_with_product_equal_n(circular_list):
    n = 851
    result = []
    length = len(circular_list)
    for start in range(length):
        for end in range(start, start + length):
            sublist = []
            product = 1
            current = start
            while current <= end:
                index = current % length
                sublist.append(circular_list[index])
                product *= circular_list[index]
                if product == n:
                    result.append(sublist.copy())
                    break
                current += 1
    return result