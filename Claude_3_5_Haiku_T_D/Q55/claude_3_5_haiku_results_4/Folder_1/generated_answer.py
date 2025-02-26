def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for start in range(n):
        for end in range(start, start + n):
            sublist = []
            product = 1
            for i in range(start, end + 1):
                index = i % n
                current = lst[index]
                sublist.append(current)
                product *= current
                if product == -51:
                    result.append(sublist.copy())
    return result