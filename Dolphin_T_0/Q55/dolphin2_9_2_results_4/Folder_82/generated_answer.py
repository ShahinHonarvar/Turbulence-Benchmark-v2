def product(lst, start, end):
    product = 1
    for i in range(start, end + 1):
        product *= lst[i % len(lst)]
    return product

def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n * 2 - 1):
        for j in range(i, n * 2):
            if j - i < n:
                if product(lst, i % n, j % n) == 8:
                    result.append(lst[i % n:j % n + 1])
    return result