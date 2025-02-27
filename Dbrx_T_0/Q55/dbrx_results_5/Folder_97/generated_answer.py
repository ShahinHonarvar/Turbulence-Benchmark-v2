from itertools import islice, cycle

def lists_with_product_equal_n(lst, n=-938):
    result = []
    for i in range(len(lst)):
        window = list(islice(cycle(lst[i:]), len(lst)))
        for j in range(1, len(window) + 1):
            if j > len(lst):
                break
            if j == 1 and window[0] == n:
                result.append([window[0]])
            elif j > 1 and window[:j] not in result and (j <= len(lst)):
                product = 1
                for k in window[:j]:
                    product *= k
                if product == n:
                    result.append(window[:j])
    return result