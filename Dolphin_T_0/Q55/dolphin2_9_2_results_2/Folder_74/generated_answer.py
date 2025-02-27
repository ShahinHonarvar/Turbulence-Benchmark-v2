def product_of_sublist(lst, n):
    length = len(lst)
    for i in range(len(lst)):
        product = 1
        for j in range(i, i + length):
            product *= lst[j % length]
            if product == n:
                yield lst[i:j + 1 % length]

def lists_with_product_equal_n(lst):
    return list(product_of_sublist(lst, 51))