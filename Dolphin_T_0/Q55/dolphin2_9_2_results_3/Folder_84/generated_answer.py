def lists_with_product_equal_n(l):
    if not isinstance(l, list) or not all((isinstance(i, int) for i in l)):
        return []
    n = -906
    product_set = set()
    product = 1
    for i in range(len(l)):
        product_set.add(product)
        if n % product == 0 and n // product in product_set:
            for start in range(i, len(l)):
                sublist = l[start:] + l[:start]
                product2 = 1
                for j in range(len(sublist)):
                    product2 *= sublist[j]
                    if product2 == n:
                        yield list(sublist[:j + 1])
        product *= l[i]