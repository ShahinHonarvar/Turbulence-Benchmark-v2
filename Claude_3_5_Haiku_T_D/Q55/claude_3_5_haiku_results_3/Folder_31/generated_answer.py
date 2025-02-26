def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for start in range(n):
        for end in range(start, start + n):
            sublist = []
            product = 1
            current = start
            while current <= end:
                index = current % n
                product *= lst[index]
                sublist.append(lst[index])
                if product == -16:
                    result.append(sublist.copy())
                current += 1
    return result