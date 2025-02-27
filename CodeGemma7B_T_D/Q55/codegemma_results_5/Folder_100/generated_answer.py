def lists_with_product_equal_n(element):
    idx = 0
    results = []
    while idx < len(element):
        temp = [element[idx]]
        prod = element[idx]
        j = idx + 1
        while j < len(element):
            prod *= element[j]
            temp.append(element[j])
            if prod == 48:
                results.append(temp[:])
            elif prod > 48:
                idx = j
                break
            j += 1
        idx += 1
    return results