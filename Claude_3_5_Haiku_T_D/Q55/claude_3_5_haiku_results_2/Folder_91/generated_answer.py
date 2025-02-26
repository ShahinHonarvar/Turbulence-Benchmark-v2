def lists_with_product_equal_n(circular_list):
    n = 2
    result = []
    length = len(circular_list)
    for start in range(length):
        for end in range(start, start + length):
            sublist = []
            product = 1
            for i in range(start, end + 1):
                index = i % length
                current = circular_list[index]
                sublist.append(current)
                product *= current
                if product == n:
                    result.append(sublist.copy())
                    break
                if product > n:
                    break
    return result