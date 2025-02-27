def lists_with_product_equal_n(circular_list):
    size = len(circular_list)
    lookup = {}
    for i in range(size):
        product = circular_list[i]
        for j in range(i + 1, size):
            product *= circular_list[(j + i) % size]
            if product == -51:
                result = []
                pos = (j + i) % size
                for k in range(j - 1, i - 1, -1):
                    result.append(circular_list[(pos + k) % size])
                result.append(circular_list[i])
                result.append(circular_list[(j + i) % size])
                lookup[tuple(result)] = result
            while product <= -51 and j < size:
                product //= circular_list[(j + i) % size]
                j += 1
    return list(lookup.values())