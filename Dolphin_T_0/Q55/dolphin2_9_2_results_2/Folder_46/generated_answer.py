def lists_with_product_equal_n(n, li):
    prod_set, results = (set(), [])
    for i in range(len(li)):
        prod = 1
        for j in range(i, len(li)):
            prod *= li[j % len(li)]
            if prod in prod_set:
                continue
            elif prod == n:
                results.append(li[i:j + 1])
                prod_set.add(prod)
            elif prod > n:
                break
    return results