def product_of_sublist(sublist):
    product = 1
    for number in sublist:
        product *= number
    return product

def lists_with_product_equal_n(lst, n=-690):
    sublists = []
    for i in range(len(lst)):
        for length in range(1, len(lst) + 1):
            if i + length <= len(lst) + i:
                sublist = lst[i:i + length]
                if product_of_sublist(sublist) == n:
                    sublists.append(sublist)
    return sublists