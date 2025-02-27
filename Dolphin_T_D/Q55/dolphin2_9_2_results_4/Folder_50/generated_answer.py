def lists_with_product_equal_n(lst):

    def check_products(lst, n):
        if len(lst) == 1 and lst[0] == 1:
            return [1]
        elif len(lst) == 1 and lst[0] == n:
            return [n]
        else:
            products = []
            for i in range(len(lst)):
                for j in range(i + 1, len(lst) + 1):
                    if functools.reduce(lambda x, y: x * y, lst[i:j]) == n:
                        products.append(lst[i:j])
            return products
    result = check_products(lst, 45)
    if not result:
        return []
    else:
        return result