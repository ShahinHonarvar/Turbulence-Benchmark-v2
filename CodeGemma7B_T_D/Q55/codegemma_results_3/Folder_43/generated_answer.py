from itertools import accumulate, filterfalse

def lists_with_product_equal_n(circ):
    """Returns a list of sublists of contiguous integers in a circular list with product equal to n."""
    productList, product, seen = ([], 1, {()})
    for i, num in enumerate(circ):
        product *= num
        productList.append(product)
    for i, product in enumerate(accumulate(productList)):
        if product in seen:
            yield list(filterfalse(lambda x: x in seen, circ[i:]))
            continue
        seen.add(product)
        productList[i] = productProduct = product
        for sublist in lists_with_product_equal_n(circ[i:]):
            if productProduct != 1 and productProduct not in sublist:
                sublist.append(productProduct)
            yield sublist