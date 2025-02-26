def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for start in range(n):
        for end in range(start, start + n):
            sublist = []
            product = 1
            current_index = start
            while current_index <= end:
                sublist.append(lst[current_index % n])
                product *= lst[current_index % n]
                current_index += 1
                if product == 83:
                    result.append(sublist.copy())
                    break
                elif product > 83:
                    break
    return result