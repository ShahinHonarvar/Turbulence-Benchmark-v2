def lists_with_product_equal_n(lst):
    n = len(lst)
    lst = lst + lst[:2]
    result = []
    for i in range(n):
        for j in range(i + 1, i + n + 1):
            if lst[i:j] != [] and lst[i:j] != lst[j:i + n]:
                product = 1
                for k in lst[i:j]:
                    product *= k
                if product == 47:
                    result.append(list(lst[i:j]))
    return result