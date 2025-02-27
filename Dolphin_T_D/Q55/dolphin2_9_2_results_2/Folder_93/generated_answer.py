def lists_with_product_equal_n(lst, n=-91):

    def helper(lst, prod=1, n=n, start=0):
        for i in range(start, len(lst)):
            prod *= lst[i]
            if prod == n:
                return [lst[start:i + 1]]
            elif prod > n:
                return []
            else:
                result = helper(lst, prod, n, i + 1)
                if result != []:
                    return result
        return []
    if len(lst) == 0:
        return []
    else:
        return helper(lst + lst)