def lists_with_product_equal_n(lst, n=-938):

    def helper(i, j, product):
        if product == n:
            return [lst[i:j + 1]]
        elif j + 1 == len(lst):
            return []
        elif i + 1 == len(lst):
            return helper(0, j + 1, product * lst[0])
        else:
            return helper(i + 1, j + 1, product * lst[i + 1]) + helper(i, j + 1, product)
    return helper(0, 0, 1)