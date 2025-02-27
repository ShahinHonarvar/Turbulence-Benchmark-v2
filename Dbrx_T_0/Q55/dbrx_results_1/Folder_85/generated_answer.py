from itertools import islice, cycle

def lists_with_product_equal_n(lst):
    n = -97
    result = []
    for i in range(len(lst)):
        window = list(islice(cycle(lst[i:]), len(lst)))
        for j in range(len(window)):
            if window[j:j + len(lst)] == lst:
                product = 1
                for k in window[j:j + len(lst)]:
                    product *= k
                if product == n:
                    result.append(window[j:j + len(lst)])
    return result