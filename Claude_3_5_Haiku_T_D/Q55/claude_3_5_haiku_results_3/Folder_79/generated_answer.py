def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        for end in range(start, start + n):
            sublist = []
            product = 1
            current = start
            while current <= end:
                index = current % n
                sublist.append(circular_list[index])
                product *= circular_list[index]
                current += 1
                if product == -83 and len(sublist) > 0:
                    result.append(sublist[:])
                    break
    return result