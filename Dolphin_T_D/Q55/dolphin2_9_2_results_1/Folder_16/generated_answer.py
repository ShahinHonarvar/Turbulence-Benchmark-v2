def lists_with_product_equal_n(lst):
    n = len(lst)
    if n == 0:
        return []
    elif n == 1 and lst[0] != -837:
        return []
    else:
        ans = []
        product = 1
        for i in range(n):
            for j in range(i + 2, n + 1):
                product *= lst[j - 1]
                if product == -837:
                    ans.append(lst[i:j])
            product = 1
        return ans