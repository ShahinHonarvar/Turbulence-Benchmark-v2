def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        for end in range(start, start + n):
            sublist = []
            product = 1
            for i in range(start, end + 1):
                index = i % n
                current = circular_list[index]
                sublist.append(current)
                product *= current
            if product == -6:
                result.append(sublist)
    return result